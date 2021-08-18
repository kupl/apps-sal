n = int(input())
arr = list(map(int, input().split()))
mi = arr[0]
ind = 0
for i in range(n):
    if(arr[i] < mi):
        mi = arr[i]
        ind = i
kol = mi
pol = kol % n
for i in range(n):
    if(kol >= arr[pol]):
        break
    kol += 1
    pol = (pol + 1) % n
print(pol + 1)
