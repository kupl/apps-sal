n = int(input())
arr = list(map(int, input().split()))
arrx = []
for i in arr:
    arrx.append(i // n)
ans = 0
arry = []
for i in range(n):
    k = arrx[i] * n
    if(arr[i] - k <= i):
        k += i + 1
    else:
        k += n + i + 1
    arry.append(k)
print(arry.index(min(arry)) + 1)
