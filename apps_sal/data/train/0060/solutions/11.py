t = int(input())
for _ in range(t):
    (a, b) = map(int, input().split())
    if a > b:
        (a, b) = (b, a)
    print(a ^ b)
