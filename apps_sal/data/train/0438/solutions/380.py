class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        bit_to_parent = [-1] * len(arr)
        size = [0] * len(arr)
        last_step = -1
        groups_of_size_m = 0

        def root(bit):
            if bit_to_parent[bit] == -1:
                return -1

            root = bit
            while root != bit_to_parent[root]:
                root = bit_to_parent[root]

            curr = bit
            while curr != root:
                tmp = bit_to_parent[bit]
                bit_to_parent[bit] = root
                curr = tmp

            # print(\"root\", bit, root)
            return root

        def union(b1, b2):
            # print(\"union\", b1, b2)
            nonlocal size
            nonlocal groups_of_size_m

            if b1 == b2:
                size[b1] = 1
                if m == 1:
                    groups_of_size_m += 1
                return

            root_b1 = root(b1)
            root_b2 = root(b2)

            if root_b1 == -1 or root_b2 == -1:
                # Can't union
                return

            if size[root_b1] >= size[root_b2]:
                parent = root_b1
                child = root_b2
            else:
                parent = root_b2
                child = root_b1

            old_parent_size = size[parent]
            old_child_size = size[child]

            size[parent] += size[child]
            bit_to_parent[child] = parent

            # print(\"union\", b1, b2, parent, child, old_parent_size, old_child_size, size[parent])
            if old_parent_size == m:
                groups_of_size_m -= 1

            if old_child_size == m:
                groups_of_size_m -= 1

            if size[parent] == m:
                groups_of_size_m += 1

            return parent

        for i in range(len(arr)):
            bit = arr[i] - 1
            bit_to_parent[bit] = bit

            union(bit, bit)
            if bit - 1 >= 0:
                union(bit, bit - 1)
            if bit + 1 < len(arr):
                union(bit, bit + 1)

            if groups_of_size_m > 0:
                last_step = i + 1

        return last_step
