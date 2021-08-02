3


def readln(): return tuple(map(int, input().split()))


n, k = readln()
a = readln()
ans = 0
for i in range(k):
    cnt = len([1 for j in range(i, n, k) if a[j] == 1])
    ans += min(cnt, n // k - cnt)
print(ans)
