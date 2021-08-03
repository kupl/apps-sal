
s = input()
ans = 0
tmp = 0
for i in s:
    if i == "A" or i == "T" or i == "G" or i == "C":
        tmp += 1
    else:
        tmp = 0
    ans = max(tmp, ans)
print(ans)
