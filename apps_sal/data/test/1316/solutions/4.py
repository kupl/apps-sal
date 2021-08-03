n, k = list(map(int, input().split()))
s = input()
c = 'abcdefghijklmnopqrstuvwxyz'
ans = 0
for ch in c:
    lvl = 0
    count = 0
    for i in s:
        if i == ch:
            count += 1
            if count == k:
                count = 0
                lvl += 1
        else:
            count = 0
    if lvl > ans:
        ans = lvl
print(ans)
