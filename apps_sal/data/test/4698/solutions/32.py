n = int(input())
t = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    (p, x) = map(int, input().split())
    t_true = t[p - 1]
    t[p - 1] = x
    print(sum(t))
    t[p - 1] = t_true
