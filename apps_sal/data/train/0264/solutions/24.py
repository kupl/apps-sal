class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return self.recursive(arr, '', 0)
        
    def recursive(self, arr, curr_str, pick_idx):
        if pick_idx == len(arr):
            table = {}
            for ch in curr_str:
                if ch in table:
                    return 0
                table[ch] = True
            return len(curr_str)
        
        return max(self.recursive(arr, curr_str + arr[pick_idx], pick_idx + 1),
                   self.recursive(arr, curr_str, pick_idx + 1))
