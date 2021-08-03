t = int(input())
for tt in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a = a[::-1]
    print(*a)
