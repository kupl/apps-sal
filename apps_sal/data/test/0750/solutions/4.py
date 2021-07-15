n, k = list(map(int, input().split()))
r_n = n * 2
g_n = n * 5
b_n = n * 8
t = 0
t += r_n // k
if r_n % k != 0:
    t += 1
t += g_n // k
if g_n % k != 0:
    t += 1

t += b_n // k
if b_n % k != 0:
    t += 1
print(t)

