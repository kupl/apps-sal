n = int(input())
s = input()
maxn = 0
now = 0
for i in s:
    if i == '+':
        now += 1
    else:
        now -= 1
    maxn = max(maxn, -now)
print(now + maxn)
