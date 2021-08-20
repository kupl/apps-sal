dio1 = [0] * 1999
dio2 = [0] * 1999
n = int(input())
for i in range(n):
    (x, y) = [int(i) for i in input().split()]
    dio1[x + y - 2] += 1
    dio2[1000 - x + y - 1] += 1
ans = 0
for i in range(1999):
    ans += dio1[i] * (dio1[i] - 1) // 2 + dio2[i] * (dio2[i] - 1) // 2
print(ans)
