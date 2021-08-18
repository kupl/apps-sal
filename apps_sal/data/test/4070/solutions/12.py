p = int(input())
s = hex(p).upper()[2:]
ans = 0
for x in s:
    if x == '0':
        ans += 1
    if x == '8':
        ans += 2
    if x == 'A':
        ans += 1
    if x == 'B':
        ans += 2
    if x == '9':
        ans += 1
    if x == 'D':
        ans += 1
    if x == '4':
        ans += 1
    if x == '6':
        ans += 1
print(ans)
