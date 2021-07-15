n,x=map(int,input().split())
a=[int(input()) for i in range(n)]
money = sum(a)
x -= money
m = min(a)
cnt = len(a)
while 0 <= x:
  x -= m
  cnt += 1
print(cnt -1)
