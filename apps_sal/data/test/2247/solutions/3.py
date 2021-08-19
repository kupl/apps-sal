T = int(input())
for t in range(T):
    (s, a, b, c) = list(map(int, input().split()))
    x = s // c
    x += x // a * b
    print(x)
