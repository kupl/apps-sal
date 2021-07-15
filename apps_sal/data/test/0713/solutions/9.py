n, m = map(int, input().split())
gemy = min(n, m)
gemy+=1
print(gemy)
for i in range(gemy):
    print(i, gemy-1 - i)
