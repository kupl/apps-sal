n, m = map(int, input().split())
for i in range(m):
    input()
print(n // 2 * "01" + "0" * (n % 2))
