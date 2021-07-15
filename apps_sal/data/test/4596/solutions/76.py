N = int(input())
a = list(map(int,input().split()))
dev = lambda x : x/2
amari = lambda x : x % 2
for i in range(1000):
    amari_a = list(map(amari, a))
    if amari_a.count(1) > 0: break
    a = list(map(dev,a))
print(i)
