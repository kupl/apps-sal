from sys import stdin
n=int(stdin.readline())
ans = 0
for i in range(n):
    x,y = map(int, stdin.readline().split())
    ans = max(ans, x+y)
print(ans)
