(n, k) = map(int, input().split())
arr = [int(x) for x in input().split()]
if len(set(arr)) < k:
    print('NO')
else:
    print('YES')
    s = set()
    for (i, e) in enumerate(arr):
        if k and e not in s:
            print(i + 1, end=' ')
            k -= 1
            s.add(e)
