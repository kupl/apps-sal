n,k = map(int,input().split())
keta = 1
while k ** keta <= n:
    keta += 1
print(keta)
