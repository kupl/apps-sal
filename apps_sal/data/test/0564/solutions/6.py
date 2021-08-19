(n, s) = list(map(int, input().split()))
list_an = list(map(int, input().split()))
if sum(list_an) - max(list_an) <= s:
    print('YES')
else:
    print('NO')
