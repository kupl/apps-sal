t = int(input())
for i in range(t):
    n = int(input())
    a = map(int, input().split())
    b = map(int, input().split())
    print(*sorted(a))
    print(*sorted(b))
