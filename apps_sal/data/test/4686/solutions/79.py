w = input()

d = {}

for i in list(w):
    if i not in list(d.keys()):
        d[i] = 1
    else:
        d[i] += 1

ans = 'Yes'
for _, v in list(d.items()):
    if v % 2 != 0:
        ans = 'No'
        break
print(ans)
