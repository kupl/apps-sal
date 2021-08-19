__author__ = 'ruckus'
n, T, c = input().split()
n = int(n)
T = int(T)
c = float(c)
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
res_a = 0
real = 0
maxi_q = max(q)
q_n = 0
for i in range(q[-1]):
    res_a = (res_a + a[i] / T) / c
    real += a[i]
    if i >= T:
        real -= a[i - T]
    if q[q_n] == i + 1:
        q_n += 1
        r = real / T
        print(r, res_a, abs(r - res_a) / r)


# Made By Mostafa_Khaled
