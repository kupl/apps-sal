import sys
n = int(input())
#a,b = map(int, input().split())
#al = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#s=[list(map(int,input().split())) for i in range(n)]
for a in range(1, 50):
    for b in range(1, 50):
        if 3**a + 5**b == n:
            print(f'{a} {b}')
            return

print((-1))
