s = input()
t = input()
ans = len(t)
for i in range(len(s) - len(t) + 1):
    count = 0
    a = s[i:i + len(t)]
    for j in range(len(t)):
        if a[j] != t[j]:
            count += 1
    ans = min(ans, count)
print(ans)
