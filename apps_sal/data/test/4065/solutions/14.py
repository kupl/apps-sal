n = int(input())
array = list(map(int, input().split()))
temp = 1
maxi = 1
for i in range(n - 1):
    if array[i] * 2 >= array[i + 1]:
        temp += 1
        if temp > maxi:
            maxi = temp
    else:
        temp = 1
if temp > maxi:
    maxi = temp
print(maxi)
