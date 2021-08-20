class Solution:

    def numTeams(self, a: List[int]) -> int:

        def rec(a, start, path, res):
            for i in range(start, len(a)):
                if len(path) == 0:
                    path.append(a[i])
                    rec(a, i + 1, path, res)
                    path.pop()
                elif len(path) == 1:
                    if a[i] != path[-1]:
                        path.append(a[i])
                        rec(a, i + 1, path, res)
                        path.pop()
                elif len(path) == 2:
                    if path[0] < path[1] and path[1] < a[i]:
                        path.append(a[i])
                        res[0] += 1
                        path.pop()
                    elif path[0] > path[1] and path[1] > a[i]:
                        path.append(a[i])
                        res[0] += 1
                        path.pop()
            return
        res = [0]
        rec(a, 0, [], res)
        return res[0]
