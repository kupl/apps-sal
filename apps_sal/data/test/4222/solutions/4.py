n,k = list(map(int,input().split()))

sunuke = [0]*n
for _ in range(k):
    d = int(input())
    a = list(map(int,input().split()))
    for i in a:
        sunuke[i-1] += 1

print((sunuke.count(0)))

