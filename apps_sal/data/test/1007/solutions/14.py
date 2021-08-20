maxk = 100001
n = 1
zcy = []
while len(zcy) <= maxk:
    zcy.append(int(str(n) + str(n)[::-1]))
    n += 1
s = input().strip().split()
k = int(s[0])
p = int(s[1])
ans = 0
for i in range(k):
    ans = (ans + zcy[i]) % p
print(ans)
