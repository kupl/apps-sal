class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)
        else:
            if arr[0] > max(arr[1:k + 1]):
                return arr[0]
            else:
                arr = arr * 2
                count, cur, pos = 0, 1, 0
                while count < k:
                    if arr[cur] > arr[pos]:
                        count += 1
                        pos += 1
                        if pos == cur:
                            pos += 1
                    else:
                        cur += 1
                        pos = cur - 1
                        count = 0
                return arr[cur]
