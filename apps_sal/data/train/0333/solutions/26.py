class Solution:
    def minJumps(self, arr: List[int]) -> int:
        A = len(arr)
        m = defaultdict(list)
        for i, n in enumerate(arr):
            m[n].append(i)

        visited = set([-1])
        curr = set([0])

        for steps in itertools.count():
            visited.update(curr)

            if A - 1 in visited:
                return steps

            curr = {j for i in curr for j in [i - 1, i + 1] + m.pop(arr[i], []) if j not in visited}

            # curr = { k for j in curr for k in [j+1, j-1] + m.pop(arr[j], []) } - visited

        return -1
