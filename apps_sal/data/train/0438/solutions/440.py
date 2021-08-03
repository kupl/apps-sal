class UF:
    def __init__(self, n):
        self.arr = list(range(n + 1))
        self.rank = [1] * n

    def root(self, x):
        curr = x
        while curr != self.arr[curr]:
            curr = self.arr[curr]

        return curr

    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)

        if root_x == root_y:
            return

        rank_x = self.rank[root_x]
        rank_y = self.rank[root_y]

        if rank_x >= rank_y:
            self.arr[root_y] = root_x
            self.rank[root_x] += rank_y
        else:
            self.arr[root_x] = root_y
            self.rank[root_y] += rank_x


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = UF(len(arr))

        sizes = {}

        seen = set()
        last_time = None
        for i, elt in enumerate(arr):
            elt -= 1

            seen.add(elt)
            left = elt - 1
            right = elt + 1
            if left >= 0 and left in seen and right < len(arr) and right in seen:
                old_left_root = uf.root(left)
                old_right_root = uf.root(right)

                sizes[uf.rank[old_left_root]].remove(old_left_root)
                if len(sizes[uf.rank[old_left_root]]) == 0:
                    del sizes[uf.rank[old_left_root]]
                sizes[uf.rank[old_right_root]].remove(old_right_root)
                if len(sizes[uf.rank[old_right_root]]) == 0:
                    del sizes[uf.rank[old_right_root]]

                uf.union(left, elt)
                uf.union(right, elt)

            elif left >= 0 and left in seen:
                old_left_root = uf.root(left)
                sizes[uf.rank[old_left_root]].remove(old_left_root)
                if len(sizes[uf.rank[old_left_root]]) == 0:
                    del sizes[uf.rank[old_left_root]]

                uf.union(left, elt)

            elif right < len(arr) and right in seen:
                old_right_root = uf.root(right)
                sizes[uf.rank[old_right_root]].remove(old_right_root)
                if len(sizes[uf.rank[old_right_root]]) == 0:
                    del sizes[uf.rank[old_right_root]]

                uf.union(right, elt)

            new_root = uf.root(elt)
            new_rank = uf.rank[new_root]

            if new_rank not in sizes:
                sizes[new_rank] = set()
            sizes[new_rank].add(new_root)

            if m in sizes:
                last_time = i

        if last_time is None:
            return -1
        else:
            return last_time + 1
