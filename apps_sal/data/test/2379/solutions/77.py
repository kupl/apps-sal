n, k, c = map(int, input().split())
s = input()

# num 回目に働く日は l[num-1] 日目以降
l = []
num = 0  # num = len(l)
i = 0
while num < k:
    if s[i] == 'o':
        l.append(i)
        num += 1
        i += c + 1
    else:
        i += 1

# num 回目に働く日は l[num-1] 日目以前
r = []
num = 0  # num = len(r)
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
