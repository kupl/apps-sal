n = input()
t_raw = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    t = t_raw.copy()
    (p, x) = map(int, input().split())
    t[p - 1] = x
    print(sum(t))
