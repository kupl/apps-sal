def cnt(a, b):
    if a < b:
        (a, b) = (b, a)
    if b == 0:
        return 0
    if a == b:
        return 1
    return a // b + cnt(b, a % b)


(a, b) = map(int, input().split())
print(cnt(a, b))
