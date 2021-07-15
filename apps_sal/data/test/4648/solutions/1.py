# for _ in range(1):
for _ in range(int(input())):
    # n = map(int, input().split())
    n = int(input())
    # arr = list(map(int, input().split()))
    # s = input()
    x = 0
    while n % 6 == 0:
        x += 1
        n //= 6
    while n % 3 == 0:
        x += 2
        n //= 3
    if n != 1:
        x = -1
    print(x)
