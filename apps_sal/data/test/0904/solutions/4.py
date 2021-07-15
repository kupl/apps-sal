n = int(input())
s = input().split()
ans = 0
d = set()
for i in s:
    cnt = 0
    for j in i:
        if j >= 'A' and j <= 'Z':
            cnt += 1
    ans = max(cnt, ans)
print(ans)

