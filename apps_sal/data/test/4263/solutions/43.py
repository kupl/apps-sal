s = input()
t = ["A", "C", "G", "T"]
cnt = 0
ans = 0
for i in range(len(s)):
    if s[i] in t:
        cnt += 1
        if cnt > ans:
            ans = cnt
    else:
        cnt = 0
print(ans)
