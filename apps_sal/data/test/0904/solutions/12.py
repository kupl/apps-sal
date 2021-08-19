n = int(input())
s = input().split()
ans = 0
for i in s:
    tmp = 0
    for j in i:
        if ord('A') <= ord(j) <= ord('Z'):
            tmp += 1
    ans = max(tmp, ans)
print(ans)
