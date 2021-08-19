(n, m) = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))
brr = list(map(int, input().strip().split(' ')))
ans = []
for i in arr:
    if i in brr:
        ans.append(i)
for i in ans:
    print(i, end=' ')
