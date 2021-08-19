(N, A, B) = map(int, input().split())
x = y = z = a = b = sum = 0
for i in range(1, N + 1):
    x = i % 10
    y = i % 100 // 10
    z = i % 1000 // 100
    a = i % 10000 // 1000
    b = i % 100000 // 10000
    if A <= x + y + z + a + b <= B:
        sum += i
print(sum)
