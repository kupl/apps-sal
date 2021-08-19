class Solution:

    def canReach1(self, arr: List[int], start: int) -> bool:

        def rcrs(i):
            if 0 <= i < len(arr) and arr[i] >= 0:
                if arr[i] == 0:
                    return True
                arr[i] = -arr[i]
                left_able = rcrs(i + arr[i])
                right_able = rcrs(i - arr[i])
                return left_able or right_able
            return False
        return rcrs(start)

    def canReach(self, arr: List[int], start: int) -> bool:
        q = collections.deque([start])
        while q:
            i = q.popleft()
            if 0 <= i < len(arr) and arr[i] >= 0:
                if arr[i] == 0:
                    return True
                arr[i] = -arr[i]
                q.append(i + arr[i])
                q.append(i - arr[i])
        return False
