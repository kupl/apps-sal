n = int(input())
s = list(map(int, input().split()))
l = []
a = 'NO'
for i in s:
    if i not in l:
        l += [i]
l = sorted(l)
if len(l) >= 3:
    for i in range(len(l) - 2):
        if l[i] + 2 == l[i + 1] + 1 == l[i + 2]:
            a = 'YES'
print(a)

