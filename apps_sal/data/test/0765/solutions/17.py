(T, S, q) = list(map(int, input().split()))
a = 0
while T > S:
    S *= q
    a += 1
print(a)
