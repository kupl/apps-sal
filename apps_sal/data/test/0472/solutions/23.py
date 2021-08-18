def s(x):

    return sum(int(i) for i in str(x))


n = input()

l, n = 9 * len(n), int(n)

ans, m = -1, int(n ** 0.5)

for x in range(max(1, m - l), m + 1):

    if n % x == 0 and x * (x + s(x)) == n:

        ans = x

        break

print(ans)
