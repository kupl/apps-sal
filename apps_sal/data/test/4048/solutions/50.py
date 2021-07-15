n = int(input())
#a, b, c, x, y = map(int, input().split())
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]
x = 1
mn = n-1
while x**2 <= n:
    if n % x == 0:
        y = n//x
        mn = min(mn, x+y-2)
    x+=1
    
print(mn)

