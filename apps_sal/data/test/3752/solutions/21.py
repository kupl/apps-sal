[k, d, t] = input().split(' ')
k = float(k)
d = float(d)
t = float(t)

T = ((k - 1) // d + 1) * d  # 一个周期得时间
T1 = k + (T - k) * 0.5  # 一个周期所能完成得

# print(T)
# print(T1)
ans = 0
ans = ans + t // T1 * T
a = t - t // T1 * T1

# print(a)
if a < k:
    ans = ans + a
else:
    ans = ans + k + (a - k) * 2
print(ans)
