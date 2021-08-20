n = int(input())
arr = list(map(int, input().split()))
x = []
for i in range(n):
    x.append([arr[i], i])
x.sort(reverse=True)
res = []
for (v, pos) in x:
    for i in range(pos):
        if arr[i] > v:
            res.append(str(i + 1) + ' ' + str(pos + 1))
print(len(res))
print('\n'.join(res))
