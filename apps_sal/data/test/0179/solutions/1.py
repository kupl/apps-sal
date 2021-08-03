
n, x, p = list(map(int, input().split()))

smallc = 0
largec = 0

left = 0
right = n
while left < right:
    mid = (left + right) // 2
    if mid < p:
        smallc += 1
        left = mid + 1
    elif mid > p:
        largec += 1
        right = mid
    else:
        left = mid + 1

largeAv = n - x
smallAv = x - 1

#print(smallc, smallAv)
#print(largec, largeAv)

mod = 1000000007


def permutations(n, c):
    v = 1
    for i in range(n - c + 1, n + 1):
        v = (v * i) % mod
    return v


v = permutations(largeAv, largec) * permutations(smallAv, smallc) % mod
oc = n - (largec + smallc + 1)
v = v * permutations(oc, oc) % mod


#print(permutations(largeAv, largec), permutations(smallAv, smallc), permutations(oc, oc))
print(v)
