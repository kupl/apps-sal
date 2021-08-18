from collections import Counter

n, x = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

if Counter(A).most_common()[0][1] >= 2:
    print(0)
    return

setA = set(A)
B = []

for a in A:
    B.append(a & x)

ans = -1

for b, c in Counter(B).most_common():
    if c >= 2:
        if b in setA:
            ans = 1
            break
        else:
            ans = 2
    else:
        break

print(ans)
