#n = int(input())
x, a, b = list(map(int, input().split()))
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
if abs(x - a) < abs(x - b):
    print('A')
else:
    print('B')
