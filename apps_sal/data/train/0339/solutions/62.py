class Solution:
    def build_triplets(self, numbers1, numbers2):
        ret = 0
        
        
        for number1, occurrences1 in numbers1.items():
            number1 *= number1
            checked_numbers = set()
            
            
            for number2, occurrences2 in numbers2.items():
                if (number2 not in checked_numbers):
                    required = number1 // number2


                    if (required not in checked_numbers and required * number2 == number1
                        and required in numbers2):
                        if (required == number2):
                            ret += occurrences2 * occurrences1 * (occurrences1 - 1) // 2
                        else:
                            ret += occurrences2 * numbers2[required] * occurrences1

                        checked_numbers.add(required)
                        
        return ret
        
        
        
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        numbers1 = collections.Counter(nums1)
        numbers2 = collections.Counter(nums2)
        return self.build_triplets(numbers1, numbers2) + self.build_triplets(numbers2, numbers1)
