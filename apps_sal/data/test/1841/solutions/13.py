import sys
def input(): return sys.stdin.readline()


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
mark = set()
ans = []
for i in range(n - 1, -1, -1):
    mark.add(a[i])
    ans.append(len(mark))
for i in range(m):
    print(ans[n - int(input())])
