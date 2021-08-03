class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = int(arr[0])
        wins = 0

        if k > len(arr):
            return max(arr)

        while wins < k:
            p1 = int(arr[0])
            p2 = int(arr[1])
            if p1 > p2:
                winner = p1
                wins += 1
                arr.append(arr.pop(1))
            else:
                winner = p2
                wins = 1
                arr.append(arr.pop(0))

        return winner
