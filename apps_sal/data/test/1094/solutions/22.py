n = int(input())
arr = []
for i in range(n):
    line = input()
    arr.append(line)
res = []
d = {}
for i in arr[::-1]:
    if i not in d:
        res.append(i)
        d[i] = True
print('\n'.join(res))

