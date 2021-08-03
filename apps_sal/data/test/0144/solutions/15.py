import sys


n = int(input())
array = list(input())
for i in range(n):
    array[i] = int(array[i])
for i in range(sum(array) + 1):
    if sum(array) == 0 or (i != 0 and sum(array) % i == 0 and i < sum(array)):
        k = 0
        l = 0
        for j in array:
            k = k + j
            if k == i:
                k = 0
                l += 1
            elif k > i:
                break
        if k == 0 and l > 1:
            print("YES")
            return
print("NO")
