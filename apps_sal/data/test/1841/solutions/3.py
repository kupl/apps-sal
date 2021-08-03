3


def readln(): return tuple(map(int, input().split()))


n, m = readln()
a = readln()
tmp = set()
cnt = [0] * n
for i in range(n - 1, -1, -1):
    tmp.add(a[i])
    cnt[i] = len(tmp)
ans = []
for _ in range(m):
    l, = readln()
    ans.append(str(cnt[l - 1]))
print('\n'.join(ans))
