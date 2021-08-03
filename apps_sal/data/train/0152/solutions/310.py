class Solution:
    def search(s, e, m, l):
        mid = (s + e) // 2
        if s > e:
            return e
        return Solution.search(mid + 1, e, m, l) if Solution.ispossible(mid, m, l) else Solution.search(s, mid - 1, m, l)

    def ispossible(n, m, l):
        count = 1
        p = l[0]
        for i in range(1, len(l)):
            if l[i] - p >= n:
                count += 1
                p = l[i]
            if count >= m:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        return Solution.search(1, position[-1] - position[0], m, position)
