n = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(n):
    if A[i] in ans:
        for j in range(A[i] - 1, 0, -1):
            if j not in ans:
                ans.append(j)
                break
    else:
        ans.append(A[i])
print(sum(ans))
