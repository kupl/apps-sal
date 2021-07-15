t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    l=list(map(int, input().split()))
    if sum(l)==m:
        print('YES')
    else:
        print('NO')
