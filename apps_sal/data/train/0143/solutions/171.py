class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        """
            [0,1,2,2]
            ^

            [3,3,3,1,2,1,1,2,3,3,4]


        """
        n = len(tree)
        res = 0
        window = defaultdict(int)
        count = 0
        left = 0
        for idx in range(n):
            curr = tree[idx]
            if window[curr] == 0:
                count += 1
            window[curr] += 1
            if count <= 2:
                res = max(res, idx - left + 1)
            while count > 2:
                window[tree[left]] -= 1
                if window[tree[left]] == 0:
                    count -= 1
                left += 1
        return res
