tests = int(input())
for test in range(tests):
    a, b = map(int, input().split())
    print(min(a, b, (a + b) // 3))
