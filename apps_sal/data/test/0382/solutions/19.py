(N, M, Q) = [int(x) for x in input().split()]
S = input()
T = input()
A = []
pref = []
for i in range(N):
    A.append(0)
    pref.append(0)
for i in range(N):
    if S[i:i + M] == T:
        A[i] = 1
    if i > 0:
        pref[i] = pref[i - 1] + A[i]
    else:
        pref[i] = A[i]
for i in range(Q):
    (l, r) = [int(x) for x in input().split()]
    l -= 1
    r -= 1
    if r - l + 1 >= M:
        if r - M + 1 >= 0:
            if l - 1 >= 0:
                print(pref[r - M + 1] - pref[l - 1])
            else:
                print(pref[r - M + 1])
        else:
            print(0)
    else:
        print(0)
