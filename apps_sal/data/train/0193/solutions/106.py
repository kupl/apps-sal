from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # we will store the frequency of all the elements in a dictionary and from the dictionary we will pick the ones with the maximum value and remove them till we do not get half size
        # we keep two dictionaries ones from number to their frequency and another from frequency to number for better manipulation
        num_fre = defaultdict(int)
        fre_num = defaultdict(set)
        for i in range(len(arr)):
            num_fre[arr[i]] += 1
            fre_num[num_fre[arr[i]]].add(arr[i])
            if fre_num[num_fre[arr[i]] - 1] != set():
                fre_num[num_fre[arr[i]] - 1].remove(arr[i])
        
        del num_fre
        answer = set()
        removed_elements = 0
        for fre in sorted(fre_num.keys(),reverse = True):
            for element in fre_num[fre]:
                if removed_elements < len(arr) // 2:
                    removed_elements += fre
                    answer.add(element)
                else:
                    break
        return len(answer)
