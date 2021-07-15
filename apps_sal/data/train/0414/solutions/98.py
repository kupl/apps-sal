class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxlen = len(arr)
        if k > maxlen:
            return max(arr)
        wins = 0
        while True:
            first, second = arr[:2]
            if first > second:
                arr.pop(1)
                arr.append(second)
                wins += 1
            else:
                arr.pop(0)
                arr.append(first)
                wins = 1
            if wins == k:
                break
            if wins > maxlen + 1:
                break
        return arr[0]
