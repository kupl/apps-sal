n = int(input())
arrA = list(map(int, input().split()))
m = int(input())
arrB = list(map(int, input().split()))
result = 0
i = 0
j = 0
sumA = 0
sumB = 0
while (i < n and j < m):
    sumA += arrA[i]
    sumB += arrB[j]
    if (sumA == sumB):
        sumA = 0
        sumB = 0
        i += 1
        j += 1
        result += 1
    elif sumA > sumB:
        sumA -= arrA[i]
        j += 1
    else:
        sumB -= arrB[j]
        i += 1
if (j == m and i == n): 
    print(result)
else:
    print("-1")

