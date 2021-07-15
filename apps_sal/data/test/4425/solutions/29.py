n, k = map(int,input().split())

per = 0

for i in range(1,n+1):
    a = 0
    while i<k:
        a += 1
        i *= 2
    per += (1/n) * (0.5**a)

print(per)
