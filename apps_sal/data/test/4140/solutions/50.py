s = input()
n = len(s)
s0 = '01' * (n // 2)
s1 = '10' * (n // 2)
if n % 2 == 1:
    s0 += '0'
    s1 += '1'
a0 = 0
a1 = 0
for i in range(n):
    if s[i] != s0[i]:
        a0 += 1
    if s[i] != s1[i]:
        a1 += 1
print(min(a0, a1))
