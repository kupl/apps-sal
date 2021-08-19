import sys
input = sys.stdin.readline


def mii():
    return list(map(int, input().split()))


n = int(input())
a = [0] + list(mii())
diff = [a[i + 1] - a[i] for i in range(n)]
ans = []
for i in range(1, n + 1):
    good = 1
    for j in range(n - i):
        if diff[j] != diff[j + i]:
            good = 0
    if good:
        ans.append(i)
print(len(ans))
print(' '.join(map(str, ans)))
