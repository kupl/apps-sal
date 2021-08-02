n, k = list(map(int, input().split()))
kset = {str(i) for i in range(k + 1)}
myans = 0
for i in range(n):
    if kset <= set(input()):
        myans += 1
print(myans)
