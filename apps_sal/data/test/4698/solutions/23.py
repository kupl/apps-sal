n = int(input())
t = list(map(int, input().split()))
total = sum(t)
m = int(input())
for i in range(m):
    (p, x) = map(int, input().split())
    p -= 1
    print(total - t[p] + x)
