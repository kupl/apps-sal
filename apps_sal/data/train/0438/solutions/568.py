class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        mask = [0] * (n + 2)
        ans = -1
        
        i = 1
        count = 0
        for index in arr:
            total_len = 1 + mask[index - 1] + mask[index + 1]
            change_set = {index + mask[index + 1], index - mask[index - 1]}
            for ind in change_set:
                if mask[ind] == m:
                    count -= 1
            mask[index - mask[index - 1]] = total_len
            mask[index + mask[index + 1]] = total_len
            
            if total_len == m:
                count += 1
            if count > 0:
                ans = i
            i += 1
        return ans
            

