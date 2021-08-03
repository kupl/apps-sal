class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodel = [arr[0]]
        for i in range(1, len(arr)):
            nodel.append(arr[i] + max(0, nodel[i - 1]))
        onedel = [arr[0]]
        for i in range(1, len(arr)):
            onedel.append(max(nodel[i], nodel[i - 1], arr[i] + onedel[-1]))
        return max(onedel)
