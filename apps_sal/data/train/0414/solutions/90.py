class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        n = len(arr)
        winner, cnt = arr.pop(0), 0

        while True:
            tmp = arr.pop(0)
            if tmp > winner:
                arr.append(winner)
                winner, cnt = tmp, 1

            else:
                arr.append(tmp)
                cnt += 1

            if cnt == k:
                return winner
