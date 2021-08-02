n, k = list(map(int, input().split()))

s = list(input())
t = ''
for j, i in enumerate(s):
    if j == k - 1: t += i.lower()
    else: t += i
print(t)
