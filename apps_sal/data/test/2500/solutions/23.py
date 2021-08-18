
data = int(input())

array = format(data, "b")

mod = 1000000007

dynamic = [[0 for j in range(3)] for i in range(len(array) + 1)]
dynamic[0][0] = 1

for i in range(len(array)):
    for j in range(3):
        for x in range(2):
            for y in range(x, 2):
                b = (data >> i) & 1
                dynamic[i + 1][(x + y + j - b + 1) // 2] = (dynamic[i + 1][(x + y + j - b + 1) // 2] + dynamic[i][j]) % mod
print(dynamic[len(array)][0])
