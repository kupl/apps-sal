class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        st, ed, l, cnt = 0, 1, len(arr), 0
        while cnt < k:
            if ed == l:
                return arr[st]
            if arr[st] > arr[ed]:
                cnt += 1
                ed += 1
            else:
                st = ed
                ed = st + 1
                cnt = 1
        return arr[st]
