(n, m) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
(i, j) = (len(A) - 1, len(B) - 1)
res = 0
while i >= 0 and j >= 0:
    if A[i] > B[j]:
        res += 1
        i -= 1
    else:
        j -= 1
        i -= 1
res += i + 1
print(res)
