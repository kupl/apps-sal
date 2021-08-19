n = int(input())
t = [0] + list(map(int, input().split()))
s = sum(t)
m = int(input())
for _ in range(m):
    (p, x) = list(map(int, input().split()))
    print(s - t[p] + x)
