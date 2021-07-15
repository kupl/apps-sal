n = int(input())
arr = [int(s) for s in input().split()]
s = sum(arr)
if s % 2 == 0 and max(arr) * 2 <= s:
    print('YES')
else:
    print('NO')
