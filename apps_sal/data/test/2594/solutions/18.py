T = int(input())
for _ in range(T):
    (a, b) = map(int, input().split())
    if a % 2 == 1 and b % 2 == 1:
        print(a * b // 2 + 1)
    else:
        print(a * b // 2)
