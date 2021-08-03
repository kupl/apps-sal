n, m = map(int, input().split())
s = input()
l = [0] * m
a, t, p = 0, 0, 1
if 10 % m:
    for i in s[::-1]:
        l[t % m] += 1
        t += int(i) * p
        a += l[t % m]
        p = p * 10 % m
else:
    a = sum(i + 1 for i in range(n) if int(s[i]) % m < 1)
print(a)
