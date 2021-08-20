s = input()
char = 'ACGT'
now = 0
ans = 0
for i in s:
    if i in char:
        now += 1
    else:
        now = 0
    ans = max(ans, now)
print(ans)
