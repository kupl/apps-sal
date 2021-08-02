n, p = [int(x) for x in input().split()]
p -= 1
atz = 'qwertyuiopasdfghjklzxcvbnm'
if len(atz) != 26:
    print('gone wrong')
d = {}
for i in atz:
    for j in atz:
        x = abs(ord(i) - ord(j))
        x = min(x, 26 - x)
        d[(i, j)] = x
s = input()
i = 0
j = len(s) - 1
m = (n + 1) // 2
if p >= m:
    p = n - 1 - p
    s = s[::-1]
revs = s[::-1]
cost = 0
while i < j:
    #    print(s,i,j)
    cost += d[(s[i], s[j])]
    i += 1
    j -= 1
if cost == 0:
    print(cost)
    return
l = 0
#print('mid cost',cost)
while d[(s[l], revs[l])] == 0:
    l += 1
r = (n // 2) - 1
while d[(s[r], revs[r])] == 0:
    r -= 1
# print(l,r,p)
cost += r - l + min(abs(l - p), abs(r - p))
print(cost)
