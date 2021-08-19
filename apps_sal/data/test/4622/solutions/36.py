n = int(input())
lst = [int(i) for i in input().split()]
if len(set(lst)) == n:
    print('YES')
else:
    print('NO')
