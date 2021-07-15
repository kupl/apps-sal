t, k = input(), int(input())
t = t.replace('5', '0')
n, d = len(t), 1000000007
s, j = 0, 1
for i in range(n):
    if t[i] == '0': s += j
    j = (2 * j) % d
print(((pow(j, k, d) - 1) * pow(j - 1, d - 2, d) % d) * (s % d) % d)
