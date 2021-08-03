N = int(input())
A = [int(x) for x in input().split()]
A.sort(reverse=True)

s = []
i = 0
while i < N - 1:
    if len(s) == 2:
        break
    if A[i] == A[i + 1]:
        s.append(A[i])
        i += 2
    else:
        i += 1

if len(s) == 2:
    print(s[0] * s[1])
else:
    print(0)
