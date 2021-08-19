n = int(input())
s = input()
alphabets = [chr(i + 97) for i in range(26)]
l1 = [0] * (n - 1)
now = [False] * 26
for i in range(n - 1):
    now[ord(s[i]) - 97] = True
    l1[i] = now.copy()
l2 = [0] * (n - 1)
now = [False] * 26
for i in range(n - 1, 0, -1):
    now[ord(s[i]) - 97] = True
    l2[i - 1] = now.copy()
ans = 0
for i in range(n - 1):
    cnt = 0
    for j in range(26):
        if l1[i][j] and l2[i][j]:
            cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)
