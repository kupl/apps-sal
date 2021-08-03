n, m = [int(x) for x in input().split()]
arr = []
for i in range(n):
    x = input()
    arr.append([int(x[j]) for j in range(len(x))])

arr_T = list(zip(*arr))

T = [sum(x) for x in arr_T]

for i in range(n):
    if all(T[j] - arr[i][j] > 0 for j in range(m)):
        print('YES')
        break
else:
    print('NO')
