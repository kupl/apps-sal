# for _ in range(1):
for _ in range(int(input())):
    # n = int(input())
    n, x = list(map(int, input().split()))
    # arr = list(map(int, input().split()))
    # s = input()
    if (n <= 2):
        print(1)
    else:
        n -= 3
        print(n // x + 2)

