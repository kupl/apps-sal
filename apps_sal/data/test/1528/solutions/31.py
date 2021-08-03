n, x = list(map(int, input().split()))

sizes = [1]

for i in range(n):
    sizes.append(2 * sizes[i] + 3)

prev = {}


def solve(n, x):
    if (n, x) in prev:
        return prev[(n, x)]
    else:
        if n == 0:
            return 1 if x == 1 else 0
        else:
            ans = 0
            if x == sizes[n]:
                ans = 2 * solve(n - 1, sizes[n - 1]) + 1
            else:
                mid = sizes[n] // 2 + 1

                if x == mid:
                    ans = solve(n - 1, sizes[n - 1]) + 1
                elif x < mid:
                    ans = solve(n - 1, x - 1)
                else:
                    ans = solve(n - 1, sizes[n - 1]) + 1 + solve(n - 1, x - mid)

            prev[(n, x)] = ans
            return ans


print(solve(n, x))
