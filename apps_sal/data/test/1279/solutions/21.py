n,m = list(map(int,input().split()))
ai = list(map(int,input().split()))
bi = list(map(int,input().split()))
num = 0
num2 = 0
for i in range(n):
    num += int(ai[i] % 2)
for i in range(m):
    num2 += int(bi[i] % 2)
print(min(n - num,num2) + min(num, m - num2))

