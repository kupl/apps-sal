K = int(input())

a = 7
for i in range(1, K+1):
    b = a%K
    if b == 0:
        print(i)
        return
    a = b*10+7
print(-1)
