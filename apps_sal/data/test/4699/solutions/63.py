(n, k) = map(int, input().split())
d = list(input().split())
while True:
    flag2 = True
    for si in str(n):
        if si in d:
            n += 1
            flag2 = False
            break
    if flag2:
        break
print(n)
