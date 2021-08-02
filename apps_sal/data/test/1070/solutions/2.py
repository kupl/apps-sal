n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
mx = 0
temp = 1
for i in range(1, n):
    if(a[i] != a[i - 1]):
        temp += 1
    else:
        if(temp > mx):
            mx = temp
        temp = 1
print(max(temp, mx))
