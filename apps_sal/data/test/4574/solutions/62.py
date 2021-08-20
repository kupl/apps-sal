N = int(input())
A = list(map(int, input().split()))
A.sort()
i = N - 1
ans = 1
count = 0
while i >= 1:
    if A[i - 1] == A[i]:
        ans *= A[i]
        i -= 2
        count += 1
    else:
        i -= 1
    if count == 2:
        print(ans)
        break
else:
    print(0)
