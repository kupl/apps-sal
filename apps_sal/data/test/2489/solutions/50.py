from collections import Counter as c
n = int(input())
a = list(map(int, input().split()))
a.sort()
(count, a_max) = (0, a[-1])
li = [True] * (a_max + 1)
for i in a:
    if li[i] == 'x':
        count -= 1
        li[i] = 'y'
    if li[i] == True:
        count += 1
        li[i] = 'x'
    j = 2
    while i * j <= a_max:
        li[i * j] = False
        j += 1
print(count)
