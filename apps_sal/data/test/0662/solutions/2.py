n = int(input())
spec = 3
for i in range(n):
    k = int(input())
    if k == spec:
        print('NO')
        break
    spec = list(set([1, 2, 3]) - set([k, spec]))[0]
else:
    print('YES')
