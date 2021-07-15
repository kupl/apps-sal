class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        players = collections.defaultdict(int)
        for i in range(len(arr) - 1):
            if arr[0] > arr[1]:
                players[arr[0]] += 1
                if players[arr[0]] == k:
                    return arr[0]
                else:
                    arr.append(arr.pop(1))
            if arr[1] > arr[0]:
                players[arr[1]] += 1
                if players[arr[1]] == k:
                    return arr[1]
                else:
                    arr.append(arr.pop(0))
        return arr[0]
