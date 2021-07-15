n = int(input())
s = [0] * n
ans = [0] * n
used = [0] * n
q = False
for i in range(n):
    s[i] = input().strip()
for i in range(n):
    for j in range(n):
        fl = True
        if (not used[j]):
            for k in range(n):
                if s[k] not in s[j]:
                    fl = False
            if fl:
                ans[i] = s[j]
                used[j] = 1
                s[j] = ''
                break
    if ans[i] == 0:
        q = True
if not q:
    print("YES")
    print(*ans[::-1], sep = '\n')
else:
    print("NO")
