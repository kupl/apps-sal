n = int(input())
t = list(map(int, input().split()))
s = sum(t)
m = int(input())
for i in range(m):
    p, x = list(map(int, input().split()))
    print((s - t[p - 1] + x))
