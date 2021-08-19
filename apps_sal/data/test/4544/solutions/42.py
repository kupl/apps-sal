N = int(input())
A = list(map(int, input().split()))
ans = 0
A.sort()
a = 0
b = 0
c = 1
for i in range(N - 1):
    if A[i] == A[i + 1]:
        a += 1
        b += 1
        c += 1
    elif A[i] + 1 == A[i + 1]:
        if ans < a:
            ans = a
        a = b
        a += 1
        b = c
        b += 1
        c = 1
    elif A[i] + 2 == A[i + 1]:
        if ans < a:
            ans = a
        if ans < b:
            ans = b
        a = c
        a += 1
        b = 1
        c = 1
    else:
        if ans < a:
            ans = a
        if ans < b:
            ans = b
        if ans < c:
            ans = c
        a = 1
        b = 1
        c = 1
if ans < a:
    ans = a
if ans < b:
    ans = b
if ans < c:
    ans = c
print(ans)
