s = input()
l = {}
ans = "Yes"
for i in s:
    if i not in l.keys():
        l[i] = 1
    else:
        l[i] += 1
for i in l.values():
    if i != 2:
        ans = "No"
print(ans)
