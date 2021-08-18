class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        d = {}
        step = 1
        ans = -1
        s = set()

        for a in arr:

            if a not in d:

                left = d.get(a - 1, [])
                right = d.get(a + 1, [])

                s = 1

                if left:
                    s += left[0]
                    if left[0] == m:
                        ans = max(ans, step - 1)

                if right:
                    s += right[0]
                    if right[0] == m:
                        ans = max(ans, step - 1)

                if s == m:
                    ans = max(ans, step)

                d[a] = [s, step]

                if left:
                    d[a - left[0]] = [s, step]

                if right:
                    d[a + right[0]] = [s, step]

            step += 1

        return ans
