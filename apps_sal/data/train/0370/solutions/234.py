class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        parents = [-1] * (max(A) + 1)

        def find(x: int) -> int:
            if parents[x] < 0:
                return x

            parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return

            depth_x = parents[root_x]
            depth_y = parents[root_y]

            if depth_x <= depth_y:
                parents[root_y] = root_x

                if depth_x == depth_y:
                    parents[root_x] -= 1

            else:
                parents[root_x] = root_y

        def get_factor(n: int) -> list:
            ans = []

            for i in range(2, int(n**(1 / 2) + 1)):
                if n % i == 0:
                    ans.append(i)

                    d = n / i
                    if (d != i) and (d % 1 == 0):
                        ans.append(int(d))

            return ans

        for num in A:
            fact = get_factor(num)

            for v in fact:
                union(num, v)

        group = [find(num) for num in A]
        cnt = Counter(group)

        return cnt.most_common(1)[0][1]
