n = int(input())
t = list(map(int, input().split()))
st = sum(t)
m = int(input())
for i in range(m):
    p, x = list(map(int, input().split()))
    print((st - t[p - 1] + x))
