class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        N = numCourses

#         # sol1: topo sort
#         pre = [0] * N
#         O = [set() for _ in range(N)]
#         for b, a in prerequisites:
#             O[a].add(b)
#             pre[b] += 1

#         stack = [c for c in range(N) if not pre[c]]
#         done = 0
#         while stack:
#             c = stack.pop()
#             done += 1
#             for post in O[c]:
#                 pre[post] -= 1
#                 if pre[post] == 0:
#                     stack.append(post)
#         return done == N

        # sol2: dfs
        O = [set() for _ in range(N)]
        for b, a in prerequisites:
            O[a].add(b)  # it's O, not I
        visit = [0] * N

        def dfs(i):
            if visit[i] == -1:
                return False
            elif visit[i] == 1:
                return True

            visit[i] = -1
            if any(not dfs(j) for j in O[i]):  # "not" dfs(j)
                return False
            visit[i] = 1
            return True

        return all(map(dfs, range(N)))
