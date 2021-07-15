n = int(input())
arr = list(map(int, input().split()))
s1 = sum(arr)
s2 = n * (n+1) / 2
if s1 == s2:
    print('YES')
else:
    print('NO')
