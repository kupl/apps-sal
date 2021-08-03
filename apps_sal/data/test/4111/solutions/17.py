n = int(input())
a = list(map(int, input().split()))
a = [0] + a
ch = [0, 0]
nech = [0, a[1]]

for i in range(2, n + 1):
    if i % 2 == 0:
        ch.append(ch[i - 2] + a[i])
        nech.append(nech[-1])
    else:
        nech.append(nech[i - 2] + a[i])
        ch.append(ch[-1])

ans = 0
for i in range(1, n + 1):
    s1 = nech[i - 1]
    s2 = ch[i - 1]
    s1 += ch[n] - ch[i]
    s2 += nech[n] - nech[i]
    if s1 == s2:
        ans += 1

print(ans)
