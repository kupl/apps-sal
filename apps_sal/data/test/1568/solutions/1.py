(n, A, B, C, T) = map(int, input().split())
t = list(map(int, input().split()))
if C <= B:
    print(len(t) * A)
else:
    total = 0
    for ti in t:
        total += A + (T - ti) * (C - B)
    print(total)
