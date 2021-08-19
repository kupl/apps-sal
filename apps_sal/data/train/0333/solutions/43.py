class Solution:

    def minJumps(self, arr: List[int]) -> int:
        s = defaultdict(list)
        for (i, num) in enumerate(arr):
            s[num] += [i]
        q = set([0])
        seen = set()
        level = 0
        while q:
            seen.update(q)
            new_q = set()
            for i in q:
                if i == len(arr) - 1:
                    return level
                children = []
                if i + 1 < len(arr):
                    children += [i + 1]
                if i - 1 >= 0:
                    children += [i - 1]
                for j in s[arr[i]]:
                    if j != i:
                        children += [j]
                del s[arr[i]]
                for child in children:
                    if child not in seen:
                        new_q.add(child)
            level += 1
            q = new_q
