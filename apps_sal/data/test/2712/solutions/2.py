input = __import__('sys').stdin.readline
for _ in range(int(input())):
    (a, b, c) = map(int, input().split())
    print(a + b + c - 1)
