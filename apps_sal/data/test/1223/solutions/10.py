def argsort(a):
    return list(map(lambda z: z[1], sorted(zip(a, range(len(a))))))


N = int(input())
P = list(map(int, input().split()))

a = argsort(P)
left = [i for i in range(N)]
right = [i for i in range(N)]
result = 0
for i in range(1, N):
    k = a[i - 1]
    extend_left = k - 1 >= 0 and P[k - 1] < i
    extend_right = k + 1 < N and P[k + 1] < i
    if extend_left and extend_right:
        L = left[k - 1]
        R = right[k + 1]
    elif extend_left:
        L = left[k - 1]
        R = k
    elif extend_right:
        R = right[k + 1]
        L = k
    else:
        L = k
        R = k
    right[L] = R
    left[R] = L
    if L - 1 >= 0:
        if L - 2 >= 0 and P[L - 2] < i:
            LL = left[L - 2]
        else:
            LL = L - 1
        result += ((L - 1) - LL + 1) * (R - k + 1) * i
    if R + 1 < N:
        if R + 2 < N and P[R + 2] < i:
            RR = right[R + 2]
        else:
            RR = R + 1
        result += (RR - (R + 1) + 1) * (k - L + 1) * i
print(result)
