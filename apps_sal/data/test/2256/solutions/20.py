t = int(input())
for i in range (t):
    n, x, a, b = list(map(int,input().split()))
    print(min(n-1, max(a, b) - min(a, b) + x))
