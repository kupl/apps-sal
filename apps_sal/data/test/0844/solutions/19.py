import sys
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
balance_max_pos = {}
balance = 0
for (i, c) in enumerate(s):
    if c == '1':
        balance += 1
    else:
        balance -= 1
    balance_max_pos[balance] = i
ans = 0
balance = 0
if balance in balance_max_pos:
    ans = max(balance_max_pos[balance] + 1, ans)
for (i, c) in enumerate(s):
    if c == '1':
        balance += 1
    else:
        balance -= 1
    if balance in balance_max_pos:
        ans = max(balance_max_pos[balance] - i, ans)
print(ans)
