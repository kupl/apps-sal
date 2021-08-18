N = int(input())
A = list(map(int, input().split()))
total = sum(A)
if total % 2 != 0:
    print("NO")
    return

for i in range(N):
    if A[i] == 0:
        continue
    elif A[i] % 2 == 0:
        A[i] = 2
    else:
        A[i] = 1

for i in range(N):
    if A[i] < 0:
        print("NO")
        return
    elif A[i] == 0:
        continue
    elif A[i] == 1:
        A[i] = 0
        if i + 1 <= N - 1:
            A[i + 1] -= 1
    else:
        A[i] = 0

for i in range(N):
    if A[i] < 0:
        print("NO")
        return

print("YES")
