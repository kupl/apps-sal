
n = int(input())
a = list(map(int, input().split()))
s = input()

prefix = [0] * n
prefix[0] = a[0]
for i in range(1, n):
    prefix[i] = prefix[i - 1] + a[i]

last = 0
answ = 0

if len(s) > n:
    print(sum(a))
    return

for i, x in enumerate(s):
    if x == '1':
        last = i
    answ += a[i] * int(x)

total = 0
for i in range(last, 0, -1):
    if s[i] == '0':
        continue
    answ = max(answ, total + prefix[i - 1])
    total += a[i]

print(answ)
