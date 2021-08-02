n = int(input())
table = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    num = table[i][(i + 1) % n]
    num2 = table[i][(i + 2) % n]
    num3 = table[(i + 2) % n][(i + 1) % n]
    print(int((num * num2 / num3)**0.5), end=" ")
