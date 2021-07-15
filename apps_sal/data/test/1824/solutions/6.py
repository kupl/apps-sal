n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

ans1 = -1
ans2 = -1
a = b = c = 0
for i in range(n-1) :
    if A[a] == B[b] :
        a += 1
    else :
        ans1 = A[a]
        break
    b += 1
if ans1 == -1 :
    ans1 = A[-1]

a = b = c = 0
for i in range(n-2) :
    if B[b] == C[c] :
        b += 1
    else :
        ans2 = B[b]
        break
    c += 1
if ans2 == -1 :
    ans2 = B[-1]

print(ans1)
print(ans2)

