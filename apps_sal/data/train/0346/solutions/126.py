class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        preprocess = [0] * (len(nums) + 1)  # preprocess[k] = num odd numbers in nums[:k]
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                count += 1
            preprocess[i + 1] = count
        print(preprocess)
        cont_preprocess = [preprocess[0]]
        counts_cont = [1]
        last_el = preprocess[0]
        for i in range(1, len(preprocess)):
            if preprocess[i] == last_el:
                counts_cont[-1] += 1
            else:
                last_el = preprocess[i]
                cont_preprocess.append(last_el)
                counts_cont.append(1)
        result = 0
        # number of (i<j) where a[j]-a[i] == k
        left_cursor = 0
        right_cursor = 0
        while left_cursor < len(cont_preprocess):
            diff = cont_preprocess[right_cursor] - cont_preprocess[left_cursor]
            if diff < k:
                right_cursor += 1
            elif diff == k:
                result += (counts_cont[right_cursor] * counts_cont[left_cursor])
                right_cursor += 1
            else:
                left_cursor += 1
            if right_cursor == len(cont_preprocess):
                right_cursor = len(cont_preprocess) - 1
                left_cursor += 1
        return result
