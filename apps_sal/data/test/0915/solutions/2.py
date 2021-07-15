from math import floor
k = int(input())
arr = [floor(k**(1/10))] * 10
def prod(arr):
    acc = 1
    for e in arr:
        acc *= e
    return acc
for i in range(len(arr)):
    if prod(arr) >= k:
        break
    arr[i] += 1 
print("".join([arr[i]*"codeforces"[i] for i in range(10)]))

