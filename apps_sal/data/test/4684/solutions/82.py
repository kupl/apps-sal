#n = int(input())
r, g, b = list(map(str, input().split()))
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]

v = int(r+g+b)
if v % 4 == 0:
    print('YES')
else:
    print('NO')

