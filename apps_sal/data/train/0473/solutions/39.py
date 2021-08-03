class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefixes = [arr[0]]
        result = 0

        for i in range(1, n):
            prefixes.append(arr[i] ^ prefixes[-1])

        for i in range(n - 1):
            for k in range(i + 1, n):
                sub_array_xor = prefixes[k] if i == 0 else prefixes[k] ^ prefixes[i - 1]
                if sub_array_xor == 0:
                    for j in range(i + 1, k + 1):
                        left_part = prefixes[j -
                                             1] if i == 0 else prefixes[j - 1] ^ prefixes[i - 1]
                        right_part = prefixes[k] ^ prefixes[j - 1]
                        if left_part == right_part:
                            result += 1

        return result
