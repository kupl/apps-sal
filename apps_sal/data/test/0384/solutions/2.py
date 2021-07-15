n = int(input())
s = input().rstrip()
a = []
k = 0
s += 'W'
for i in s:
    if i == 'B':
        k += 1
    else:
        if k > 0:
            a.append(k)
        k = 0
print(len(a))
print(' '.join(map(str, a)))
