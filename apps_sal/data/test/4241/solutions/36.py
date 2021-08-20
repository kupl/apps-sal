s = list(input())
t = list(input())
n = len(s) - len(t) + 1
ans = 0
for i in range(n):
    count = 0
    for g in range(len(t)):
        if s[g + i] == t[g]:
            count += 1
    if count >= ans:
        ans = count
print(len(t) - ans)
