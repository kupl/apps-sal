class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        count = collections.defaultdict(int)
        while True:
            if arr[0] > arr[1]:
                count[arr[0]] += 1
                if count[arr[0]] == k:
                    return arr[0]
                arr.append(arr[1])
                arr.remove(arr[1])
            else:
                count[arr[1]] += 1
                if count[arr[1]] == k:
                    return arr[1]
                arr.append(arr[0])
                arr.remove(arr[0])
