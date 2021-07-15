n = int(input())
s = input()
ans = 0
for i in range(1, n+1):
    cnt = 0
    x = s[0:i]
    y = s[i:n+1]
    for j in range(97, 123):
        if chr(j) in x and chr(j) in y:
            cnt += 1
    ans = max(cnt, ans)
print(ans)
