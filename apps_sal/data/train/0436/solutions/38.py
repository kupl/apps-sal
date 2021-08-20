class Solution:

    def minDays(self, n: int) -> int:

        def bfs(n):
            (q1, q2) = ([n], [0])
            (seen1, seen2) = ({n: 0}, {0: 0})
            (step1, step2) = (0, 0)
            while q1 or q2:
                p1 = []
                p2 = []
                step1 += 1
                step2 += 1
                while q1:
                    curr1 = q1.pop()
                    if curr1 in seen2:
                        return seen1[curr1] + seen2[curr1]
                    if curr1 % 3 == 0:
                        nx = curr1 // 3
                        if nx not in seen1:
                            seen1[nx] = step1
                            p1.append(nx)
                    if curr1 % 2 == 0:
                        nx = curr1 // 2
                        if nx not in seen1:
                            seen1[nx] = step1
                            p1.append(nx)
                    if curr1 - 1 not in seen1:
                        seen1[curr1 - 1] = step1
                        p1.append(curr1 - 1)
                while q2:
                    curr2 = q2.pop()
                    if curr2 in seen1:
                        return seen1[curr2] + seen2[curr2]
                    for nx in [curr2 * 3, curr2 * 2, curr2 + 1]:
                        if nx <= n and nx not in seen2:
                            seen2[nx] = step2
                            p2.append(nx)
                (q1, q2) = (p1, p2)
            return -1
        return bfs(n)
