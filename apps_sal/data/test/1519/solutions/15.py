n, l, a = map(int, input().split())
T = 0
k = 0
for i in range(n):
    t, li = map(int, input().split())
    k += (t - T) // a
    T = t + li
k += (l - T) // a
print(k)
