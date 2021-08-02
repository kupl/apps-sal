s1 = input()
s2 = input()
n, m = len(s1), len(s2)
t, res = 0, [0, 0]
for i in range(m):
    t ^= (s1[i] == '0')
    t ^= (s2[i] == '0')
res[t] += 1
for i in range(m, n):
    t ^= (s1[i] == '0') ^ (s1[i - m] == '0')
    res[t] += 1
print(res[0])
