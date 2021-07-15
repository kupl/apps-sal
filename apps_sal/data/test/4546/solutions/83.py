#n = int(input())
a, b, c = list(map(int, input().split()))
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

if b-a == c-b:
    print('YES')
else:
    print('NO')

