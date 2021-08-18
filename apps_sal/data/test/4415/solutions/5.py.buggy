import sys

n = int(input())
A = list(map(int, input().split()))
A.sort()

ANS0 = [A[0]]
ANS1 = []
for i in range(1, n):
    if A[i] == ANS0[-1]:
        ANS1.append(A[i])

    else:
        ANS0.append(A[i])

for i in range(1, len(ANS1)):
    if ANS1[i] == ANS1[i - 1]:
        print("NO")
        return

print("YES")
print(len(ANS0))
print(*ANS0)
print(len(ANS1))
print(*ANS1[::-1])
