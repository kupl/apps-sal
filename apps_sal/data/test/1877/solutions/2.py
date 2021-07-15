n = int(input())
s = input()
bal = 0
last = 0
ans = 0
for i in s:
    if i == 'U':
        bal += 1
    else:
        bal -= 1
    if bal == 0:
        continue
    if last * bal < 0:
        ans += 1
    last = bal
print(ans)
