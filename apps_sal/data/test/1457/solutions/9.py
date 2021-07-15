t = input()
p = input()
s = p + '&' + t 
n = len(s)
k = len(p)
z = [0] * n
l = 0
r = 0
for i in range(1, n):
    if i <= r:
        z[i] = min(r - i + 1, z[i - l])
    while i +z[i] < n and s[z[i]] == s[i + z[i]]:
        z[i] += 1
    if i + z[i] - 1 > r:
        r = i + z[i] - 1
        l = i
ans = 0
i = len(p) - 1
while i < n:
    if z[i] == len(p):
        ans += 1
        i += k
    else:
        i += 1

print(ans)

