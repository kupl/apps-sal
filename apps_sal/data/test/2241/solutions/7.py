(n, j) = (int(input()), 0)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    if b[i] > a[i] * 2 or b[i] == 1:
        j -= 1
    else:
        j += b[i] // 2 * (b[i] - b[i] // 2)
print(j)
