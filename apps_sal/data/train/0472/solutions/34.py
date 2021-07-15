class Solution:
    def canReach1(self, arr: List[int], start: int) -> bool:
        # recursive helper function
        # recurse both left, right from i-th position
        # invert arr value to check only once
        # O(N) time, space in recursive stack

        def rcrs(i):
            if (0 <= i < len(arr)) and (arr[i] >= 0):
                if arr[i] == 0:
                    return True

                arr[i] = -arr[i]
                left_able = rcrs(i + arr[i])
                right_able = rcrs(i - arr[i])
                return left_able or right_able
            return False

        # recursive call
        return rcrs(start)

    def canReach(self, arr: List[int], start: int) -> bool:
        # try iteratively: add values to deque w/ value inversion
        # O(N) time, O(N) space

        q = collections.deque([start])

        while q:
            i = q.popleft()

            if (0 <= i < len(arr)) and arr[i] >= 0:
                if arr[i] == 0:
                    return True

                arr[i] = -arr[i]
                q.append(i+arr[i]) # left
                q.append(i-arr[i]) # right
        return False
