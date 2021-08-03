n = int(input())
u = []
s = [int(i) for i in input().split()]
s.sort()
s.append(6001)
n += 1
k = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        u.append(i)
    elif u and s[i] + 1 < s[i + 1]:
        t = s[i] + 1
        while t < s[i + 1] and u:
            k += (t - s[u.pop(0)])
            t += 1
print(k)
