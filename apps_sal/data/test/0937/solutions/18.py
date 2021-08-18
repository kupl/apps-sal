L = input().split()
n, m = list(map(int, L))
L = input().split()
a = list(map(int, L))
L = input().split()
t = list(map(int, L))
ttot = [0] * (n + 5)
ttot[0] = 0
ta = [0] * (n + 5)
ta[0] = 0
for i in range(n):
    ttot[i + 1] = ttot[i] + a[i]
    ta[i + 1] = ta[i] + a[i] * t[i]
Max = 0
for i in range(n - m + 1):
    tmp = ta[i]
    tmp = tmp + ttot[i + m] - ttot[i]
    tmp = tmp + (ta[n] - ta[i + m])
    if (tmp > Max):
        Max = tmp
        pos = i + 1
print(Max)
