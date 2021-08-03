# n : 全日数　k：働く日数　c：働いた日からその後働かない日数
n, k, c = map(int, input().split())
s = input()

# 前から貪欲的に働く日を求める l
l = []
i = 0
num = 0
while num < k:
    if s[i] == 'o':
        l.append(i)
        num += 1
        i += c + 1
    else:
        i += 1

# 後ろから貪欲的に働く日を求める r
r = []
num = 0
i = n - 1
while num < k:
    if s[i] == 'o':
        r.append(i)
        num += 1
        i -= c + 1
    else:
        i -= 1
r.reverse()

for i in range(k):
    if l[i] == r[i]:
        print(l[i] + 1)
