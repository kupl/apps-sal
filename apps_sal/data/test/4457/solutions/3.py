import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
ls = list(map(int, input().split()))
ls = [(i, ls[i-1]) for i in range(1, n+1)]
ls.sort(key=lambda x: x[1])
ls.reverse()
cnt = 0
for i in range(n):
    cnt+=i*ls[i][1]+1
print(cnt)
for i in range(n):
    print(ls[i][0], end=' ')
print()

