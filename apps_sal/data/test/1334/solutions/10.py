(n, k) = list(map(int, input().split()))
s = input().strip()
cnt = [0] * 26
for i in s:
    cnt[ord(i) - 97] += 1
lo = 0
hi = 25
for i in range(0, 26):
    if cnt[i] != 0:
        lo = i
        break
for i in range(25, -1, -1):
    if cnt[i] != 0:
        hi = i
        break
if k <= n:
    ans = list(s[:k])
    for j in range(k - 1, -1, -1):
        done = 0
        for i in range(ord(s[j]) - 97 + 1, 26):
            if cnt[i] != 0:
                ans[j] = chr(i + 97)
                done = 1
                break
        if done:
            for z in range(j + 1, k):
                ans[z] = chr(lo + 97)
            break
else:
    ans = list(s)
    for i in range(k - n):
        ans.append(chr(lo + 97))
print(''.join(ans))
