class Solution:

    def find(self, node1: int, group: List[int]) -> int:
        head = node1
        while head != group[head]:
            head = group[head]
        return head

    def union(self, node1: int, node2: int, group: List[int], size: dict) -> int:
        (head1, head2) = (self.find(node1, group), self.find(node2, group))
        if head1 == head2:
            return head1
        if size[head1] < size[head2]:
            group[head1] = head2
            size[head2] += size[head1]
            size.pop(head1)
            return head2
        group[head2] = head1
        size[head1] += size[head2]
        size.pop(head2)
        return head1

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        group = [-1 for _ in range(len(arr))]
        sizes = {}
        ans = -1
        arr_size = len(arr)
        for (ix, val) in enumerate(arr):
            if group[val - 1] != -1:
                continue
            group[val - 1] = val - 1
            sizes[val - 1] = 1
            for neighbor in (val - 2, val):
                if 0 <= neighbor < arr_size:
                    head = self.find(neighbor, group)
                    if head in sizes and sizes[head] == m:
                        ans = ix
                    if group[neighbor] != -1:
                        self.union(val - 1, neighbor, group, sizes)
        return ans
