

def is_cycle(seq, k):
    ii = 0
    for i in range(len(seq)):
        if ii == k:
            ii = 0
        if seq[i] != seq[ii]:
            return False
        ii += 1
    return True


n = int(input())

A = [0] + [int(x) for x in input().split()]

AA = []
for i in range(1, len(A)):
    AA.append(A[i] - A[i - 1])

cyqs = []
for cyq in range(1, len(A)):
    if is_cycle(AA, cyq):
        cyqs.append(cyq)
print(len(cyqs))
print(*cyqs)
