N = int(input())
A = list(map(int, input().split()))

ans = []


def f1():
    for i in range(1, N):
        mx = -(10**7)
        mxi = 0
        for j in range(N):
            if A[j] > mx:
                mx = A[j]
                mxi = j
        A[i] += mx
        ans.append((mxi, i))


def f2():
    for i in range(N - 2, -1, -1):
        mn = 10**7
        mni = 0
        for j in range(N):
            if A[j] < mn:
                mn = A[j]
                mni = j
        A[i] += mn
        ans.append((mni, i))


mx = -(10**7)
mxi = 0
mn = 10**7
mni = 0
for i in range(N):
    if A[i] > mx:
        mx = A[i]
        mxi = i
    if A[i] < mn:
        mn = A[i]
        mni = i
if mn >= 0:
    f1()
elif mx <= 0:
    f2()
elif mx >= abs(mn):
    for i in range(N):
        if A[i] < 0:
            A[i] += mx
            ans.append((mxi, i))
    f1()
else:
    for i in range(N):
        if A[i] > 0:
            A[i] += mn
            ans.append((mni, i))
    f2()

print((len(ans)))
for a1, a2 in ans:
    print((a1 + 1, a2 + 1))
