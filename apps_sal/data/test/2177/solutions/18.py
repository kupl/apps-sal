t = int(input())
for i in range(t):
    (a, b) = list(map(int, input().strip().split()))
    c = len(str(b))
    if b != int('9' * c):
        c = c - 1
    print(a * c)
