def check():
    nonlocal n, k, A, B
    a = k
    h = 0
    for i in range(n):
        if k < 0:
            h = 1
            break
        else:
            if B[i] >= A[i]:
                B[i] -= A[i]
            else:
                if B[i] + k < A[i]:
                    h = 1
                    break
                else:
                    k -= (A[i] - B[i])
                    B[i] = 0

    if h == 1:
        return False
    else:
        return True


n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
p = 0
while check():
    p += 1
print(p)
