class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        import collections
        fruits = collections.defaultdict(int)
        max_len = 0
        front = back = 0
        while back < len(tree):
            if len(list(fruits.keys())) <= 2:
                fruits[tree[back]] += 1
                back += 1
            else:
                fruits[tree[front]] -= 1
                if fruits[tree[front]] == 0:
                    del fruits[tree[front]]
                front += 1
            if len(list(fruits.keys())) <= 2:
                max_len = max(max_len, back - front)
        return max_len
