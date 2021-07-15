from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    n,x = list(map(int,input().split()))
    a = sorted(list(map(int,input().split())),reverse=True)
    g = a.pop()
    ans = 0
    for i in a:
        ans += max(0,(x-i)//g)
    print(ans)

