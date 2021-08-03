import sys
input = sys.stdin.readline


def judge(i, x):
    return acc[min(n, i + x + 1)] - acc[max(0, i - x)] >= k + 1


def binary_search(i):
    l, r = 0, n

    while l <= r:
        mid = (l + r) // 2

        if judge(i, mid):
            r = mid - 1
        else:
            l = mid + 1

    return l


n, k = map(int, input().split())
S = input()[:-1]
acc = [0]

for Si in S:
    acc.append(acc[-1] + (1 if Si == '0' else 0))

ans = n

for i in range(n):
    if S[i] == '0':
        ans = min(ans, binary_search(i))

print(ans)
