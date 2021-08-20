class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) < k:
            return max(arr)
        if k == 1:
            return max(arr[0], arr[1])
        cnt = 0
        while arr and cnt < k:
            j = 1
            while arr[0] > arr[j]:
                cnt += 1
                j += 1
                if cnt == k:
                    return arr[0]
            arr.append(arr[0])
            arr.pop(0)
            cnt = 1
