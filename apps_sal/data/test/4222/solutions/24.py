n, k= map(int, input().split())

sunuke = [1] * n

for i in range(k):
    d = int(input())
    oka = map(int,input().split())
    for j in oka:
        sunuke[j-1] = 0
        
print(sum(sunuke))
