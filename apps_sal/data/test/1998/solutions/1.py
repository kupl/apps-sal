n, a, b, k = map(int, input().split())
s = input()
ind = 0
ans = []

for i in range(k):
    l = s[ind:].find("1")
    if (l) >= b:
        ans.append([l, ind, ind + l])
    ind += l + 1

if (len(s) - ind) >= b:
    ans.append([len(s) - ind, ind, len(s)])

aans = []
count = 0
for i in range(len(ans)):
    j = ans[i][1] - 1
    while j + b < ans[i][2]:
        j += b
        aans.append(j + 1)

l = len(aans) - a + 1
aans = aans[:l]
print(len(aans))
print(*aans)
