N, M = list(map(int, input().split()))
arraybi = list(map(int, input().split()))
arraylamp = list(range(1,N+1))
num = 0
array = ""
for lamp in arraylamp:
    while arraybi[num] > lamp:
        num += 1
    array += str(arraybi[num]) + " "
    num = 0
print(array)

