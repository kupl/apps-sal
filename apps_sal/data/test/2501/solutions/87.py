n = int(input())
a = list(map(int, input().split()))
count = {}
for i in range(len(a)):
    minus = i + 1 - a[i]
    if minus in count:
        count[minus] += 1
    else:
        count[minus] = 1
total = 0
for i in range(len(a)):
    plus = a[i] + (i + 1)
    if plus in count:
        total += count[plus]
print(total)
