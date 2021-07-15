from math import *
N = int(input())
A = list(map(int, input().split()))


ans = 0

for i in range(1, len(A)):
    if A[i] == A[i-1]:
        ans = inf
        break
    if (A[i] == 2 and A[i-1] == 3) or (A[i] == 3 and A[i-1] == 2):
        ans = inf
        break
if ans == inf:
    print("Infinite")
else:

    for i in range(1, len(A)):
        if A[i] == 1 and A[i-1] == 3:
            ans += 4
        elif A[i] == 1 and A[i-1] == 2:        
            ans += 3
        elif A[i] == 2:
            if i < 2 or A[i-2] != 3:
                ans += 3
            else:
                ans += 2
        else:
            ans += 4

    print("Finite")
    print(ans)
