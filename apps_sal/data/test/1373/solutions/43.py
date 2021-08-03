n, k = map(int, input().split())
L = list(range(n + 1))

cnt = 0
ans = 0


def calc(i):
    smallest = (i - 1) * i // 2
    largest = (2 * n - i + 1) * i // 2
    return largest - smallest + 1


for i in range(k, n + 2):
    cnt += calc(i)
    cnt %= (10**9 + 7)


print(cnt)
