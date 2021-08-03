n, k = list(map(int, input().split()))

zeroes = 0
deletes = 0

good = False

for c in str(n)[::-1]:
    if c == "0":
        zeroes += 1
        if zeroes == k:
            good = True
            break
    else:
        deletes += 1

if good:
    print(deletes)
elif zeroes >= 1:
    print(len(str(n)) - 1)
