n, k = input().split()
hate = list(input().split())
exi = True
t = True

while True:
    for c in hate:
        t = True
        if c in list(n):
            t = False
            break
    if t:
        print(n)
        break

    intN = int(n) + 1
    n = str(intN)
