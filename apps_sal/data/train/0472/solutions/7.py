class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited_indices = set()

        def visit(index: int):
            if index < 0 or index >= len(arr):
                return False

            if index in visited_indices:
                return False
            if arr[index] == 0:
                return True
            visited_indices.add(index)

            a = visit(index + arr[index])
            b = visit(index - arr[index])
            return a or b

        return visit(start)
