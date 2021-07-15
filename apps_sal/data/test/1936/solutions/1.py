# for _ in range(1):
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    # n = int(input())
    # arr = list(map(int, input().split()))
    # s = input()
    if 2 * a > b:
        print(-1, -1)
    else:
        print(a, 2 * a)


