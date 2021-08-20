class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        i = 0
        if k > len(arr):
            return max(arr)
        t = k
        (p1, p2) = (arr[0], arr[1])
        while t:
            if p1 > p2:
                arr.pop(1)
                arr.append(p2)
                p2 = arr[1]
                t -= 1
            else:
                arr.pop(0)
                arr.append(p1)
                p1 = arr[0]
                p2 = arr[1]
                t = k - 1
        return p1
