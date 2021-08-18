t = int(input())
for i in range(t):
    a, b, k = list(map(int, input().split()))
    num0 = k // 2
    num1 = k - num0
    print(num1 * a - num0 * b)
