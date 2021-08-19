n = int(input())
s = input()
count = 1
i = 0
ans = ''
for c in s:
    if i == 0:
        ans += c
    i += 1
    if i == count:
        i = 0
        count += 1
print(ans)
