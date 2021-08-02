s = input()
k = int(input())
c = []
for i in range(len(s)):
    for j in range(k): c.append(s[i:i + j + 1])
c.sort()
pre = ''
for x in c:
    if pre == x: continue
    k -= 1
    if k == 0:
        print(x)
        break
    pre = x
