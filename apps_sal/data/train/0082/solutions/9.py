t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.reverse()
    print(*l)
