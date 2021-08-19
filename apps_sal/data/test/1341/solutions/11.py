s = str(input())
t = str(input())
idx = 0
ans = s[idx]
for i in range(len(t)):
    if ans == t[i]:
        idx += 1
        ans = s[idx]
print(idx + 1)
