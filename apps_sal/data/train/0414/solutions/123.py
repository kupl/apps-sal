class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        m = collections.defaultdict(int)
        (first, second) = (0, 1)
        while second < len(arr):
            if arr[first] < arr[second]:
                first = second
                m[arr[second]] += 1
                if m[arr[second]] == k:
                    return arr[second]
                second += 1
            else:
                m[arr[first]] += 1
                if m[arr[first]] == k:
                    return arr[first]
                second += 1
        return max(arr)
