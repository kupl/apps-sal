n = int(input())
a = list(map(int,input().split()))
x = 0
t = True
while t:
    for i in range(n):
        if a[i] % 2 == 1:
            t = False
        a[i] /= 2
    x += 1
print(x-1)
