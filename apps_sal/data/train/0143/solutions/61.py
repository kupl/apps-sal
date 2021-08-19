class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # max contiguous sum with 2 different types of elements

        start = 0
        end = 0
        le = len(tree)
        hmap = collections.defaultdict(int)
        count = 0
        res = 0

        while end < le:

            hmap[tree[end]] += 1
            if hmap[tree[end]] == 1:
                count += 1

            end += 1

            while count > 2 and start < end:
                hmap[tree[start]] -= 1
                if hmap[tree[start]] == 0:
                    count -= 1
                start += 1

            if count > 2:
                continue

            res = max(res, end - start)

        return res
