n = int(input())
cash = {}
for i in range(n):
    key = input()
    if key in cash:
        cash[key] += 1
    else:
        cash[key] = 1
maxm = 0
for key in cash:
    if cash[key] > maxm:
        maxm = cash[key]
print(maxm)
