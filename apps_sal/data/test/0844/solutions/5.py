n = int(input())
s = input()
bal = 0
arr = [0] * (n + 1)
lastseen = {0: 0}
arr[0] = 0
for i in range(1, n + 1):
    if s[i - 1] == '1':
        bal += 1
    else:
        bal -= 1
    lastseen[bal] = i
    arr[i] = bal
ans = 0
for i in range(n + 1):
    if lastseen[arr[i]] != i:
        ans = max(ans, lastseen[arr[i]] - i)
print(ans)
