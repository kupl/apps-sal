class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def possible(num):
            (Count, pos) = (1, 0)
            for i in range(1, len(position)):
                if position[i] - position[pos] >= num:
                    pos = i
                    Count += 1
                if Count == m:
                    return True
            return Count >= m

        def search(left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if possible(mid) and (not possible(mid + 1)):
                return mid
            elif possible(mid):
                return search(mid + 1, right)
            return search(left, mid - 1)
        return search(1, position[-1] - position[0])
