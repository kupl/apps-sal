t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    print(min(a[-2]-1, n-2))

