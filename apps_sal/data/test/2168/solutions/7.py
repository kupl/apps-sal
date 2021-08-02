t = int(input())
arr = []
data = []
maxi = 0
for i in range(t):
    arr1 = list(map(int, input().split()))
    n = arr1[0]
    em = arr1[1:]
    em.sort()

    arr.append(n)
    data.append(em[-1])
    if(maxi < em[-1]):
        maxi = em[-1]

inc = 0
for i in range(t):
    dif = maxi - data[i]
    if(dif != 0):
        inc = inc + dif * arr[i]

print(inc)
