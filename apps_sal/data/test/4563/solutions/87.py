n = int(input())
t_v = a_v = 1
for _ in range(n):
    t, a = [int(x) for x in input().split()]
    r = max((t_v + t - 1) // t, (a_v + a - 1) // a)
    t_v, a_v = r * t, r * a
print(t_v + a_v)
