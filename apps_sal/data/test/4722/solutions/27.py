#n = int(input())
a, b = list(map(int, input().split()))
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

if a % 3 == 0 or b % 3 == 0 or (a+b) % 3 == 0:
    print('Possible')
else:
    print('Impossible')

