import collections


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        self.m = collections.defaultdict(list)

        for ix_1 in range(len(arr)):
            set_1 = set(list(arr[ix_1]))
            for ix_2 in range(ix_1 + 1, len(arr)):
                set_2 = set(list(arr[ix_2]))
                if len(set_1) == len(arr[ix_1]) and len(set_2) == len(arr[ix_2]) and len(set_1.intersection(set_2)) == 0:
                    self.m[ix_1].append(ix_2)
                    # self.m[ix_2].append(ix_1)

        self.ans = 0
        for ix in range(len(arr)):
            if len(set(list(arr[ix]))) == len(arr[ix]):
                self.dfs(arr, [ix])

        return self.ans

    def dfs(self, arr, visiting):
        curr = visiting[-1]

        l = [len(arr[i]) for i in visiting]
        self.ans = max(sum(l), self.ans)

        if not self.m.get(curr):
            return

        for i in self.m.get(curr):
            if i in visiting:
                continue

            possible = True
            for j in visiting[:-1]:
                if len(set(list(arr[i])).intersection(set(list(arr[j])))) > 0:
                    possible = False
                    break

            if possible:
                visiting.append(i)
                self.dfs(arr, visiting)
                visiting.pop()
