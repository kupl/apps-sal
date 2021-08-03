t = int(input())

for case in range(t):
    a, b, c = list(map(int, input().split()))
    arr = list(sorted([a, b, c]))
    minsm = a + b
    min_len = abs(c - minsm)
    print(min_len + 1)
