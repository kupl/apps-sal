class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr) - 2:
            return max(arr)
        if len(arr) < 3:
            return max(arr)
        left = arr[0]
        right = arr[1]
        d = collections.deque(arr[2:])
        count = 0
        while count < k:
            if left > right:
                count += 1
                d.append(right)
            else:
                count = 1
                d.append(left)
                left = right
            right = d.popleft()
        return left
