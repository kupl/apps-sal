class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        p1 = 0
        p2 = 0
        counter = 0
        mx = 0
        mmap = {}
        uniq = set()
        while p2 < len(tree):
            if len(uniq) > 2:
                mmap[tree[p1]] -= 1
                if mmap[tree[p1]] == 0:
                    uniq.remove(tree[p1])
                p1 += 1
            else:
                if tree[p2] in mmap:
                    mmap[tree[p2]] += 1
                else:
                    mmap[tree[p2]] = 1
                uniq.add(tree[p2])
                if len(uniq) <= 2:
                    counter = p2 - p1 + 1
                mx = max(mx, counter)
                p2 += 1
        return mx
