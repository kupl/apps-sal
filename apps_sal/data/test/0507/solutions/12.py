def check(A, B):
    diff = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            diff += 1
    return diff == 1


def ip():
    return list(map(int, input().split()))


n = int(input())
A = ip()
B = ip()
diff = 0
left = set(range(1, n + 1))
C = [0 for _ in range(n)]
for i in range(n):
    if A[i] == B[i]:
        C[i] = A[i]
        if A[i] in left:
            left.remove(A[i])
    else:
        diff += 1
if diff == 1:
    for i in range(n):
        if C[i] == 0:
            C[i] = left.pop()
else:
    (i, j) = [k for k in range(n) if C[k] == 0]
    left = list(left)
    assert diff == 2
    assert len(left) == 2
    C[i] = left[0]
    C[j] = left[1]
    if not check(A, C) or not check(B, C):
        C[i] = left[1]
        C[j] = left[0]
print(*C)
