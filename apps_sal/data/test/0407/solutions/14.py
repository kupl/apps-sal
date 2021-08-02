num = []

for i in range(10):
    num.append([])
    num[i].append(1)
    num[i].append(0)

n = int(input())
for kk in range(n):
    s = input()
    num[ord(s[0]) - 97][0] = 0
    for i in range(len(s)):
        num[ord(s[i]) - 97][1] += pow(10, len(s) - i - 1)

num = sorted(num, key=lambda s: s[1], reverse=True)

boo = True
ans = 0
now = 1

for i in range(10):
    if boo and num[i][0] == 1:
        ans += 0
        boo = False
    else:
        ans += num[i][1] * now
        now += 1

print(ans)
