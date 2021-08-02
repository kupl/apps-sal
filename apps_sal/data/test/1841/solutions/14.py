import sys
def input(): return sys.stdin.readline()


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
mark = [0] * 100001
ans = [0] * 100001
for i in range(n - 1, -1, -1):
    ans[i] = ans[i + 1] + 1 - mark[a[i]]
    mark[a[i]] = 1
for i in range(m):
    print(ans[int(input()) - 1])
