class Solution:
    def minDays(self, n: int) -> int:
        queue = [(n, 0)]
        visited = set()
        while queue:
            remain, day = queue.pop(0)
            if remain == 0:
                return day
            if remain % 2 == 0 and remain // 2 not in visited:
                queue.append((remain // 2, day + 1))
                visited.add(remain // 2)
            if remain % 3 == 0 and remain // 3 not in visited:
                queue.append((remain // 3, day + 1))
                visited.add(remain // 3)
            if remain - 1 not in visited:
                queue.append((remain - 1, day + 1))
