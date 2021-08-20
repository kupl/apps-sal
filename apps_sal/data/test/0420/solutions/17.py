(n, m) = map(int, input().split())
matrix = []
for i in range(n):
    arr = list(map(int, input().split()))
    matrix.append(arr)
while n and n & 1 == 0:
    t = n // 2
    flag = True
    for i in range(n):
        if matrix[i] != matrix[n - 1 - i]:
            flag = False
    if flag == False:
        break
    else:
        n >>= 1
print(n)
