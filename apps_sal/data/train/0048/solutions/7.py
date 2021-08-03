tests = int(input())
for test in range(tests):
    a = 1
    x, y, k = list(map(int, input().split()))
    a1 = (k * (y + 1) - 1 + x - 2) // (x - 1)
    print(a1 + k)
