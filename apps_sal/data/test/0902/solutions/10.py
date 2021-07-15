


n, k = list(map(int, input().split()))
A = [int(x) for x in input().split()]

A.reverse()

cc = A.pop()
cr = 0

while len(A) > 0 and cc != n and cr < k:
    nc = A.pop()
    if nc > cc:
        cc = nc
        cr = 1
    else:
        cr += 1

print(cc)

