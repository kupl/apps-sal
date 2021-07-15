n = int(input())
s = list(map(int,input().split()))
temp = len(s)
ans = len(list(set(s)))
if temp == ans:
    print('YES')
else:
    print('NO')
