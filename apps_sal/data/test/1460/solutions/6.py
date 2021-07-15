# n, k = map(int, input().split())
n = int(input())
print(3 * n + 4)
print(0, 0)
for x in range(n + 1):
    print(x + 1, x)
    print(x + 1, x + 1)
    print(x, x + 1)

