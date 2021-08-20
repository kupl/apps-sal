n = int(input())
A = list(map(int, input().split()))
ans = [0] * n
for i in range(n)[::-1]:
    if i >= n // 2:
        ans[i] = A[i]
    else:
        tmp = 0
        j = i + 1
        while j <= n:
            tmp += ans[j - 1]
            j += i + 1
        if A[i] == 1:
            if tmp % 2 != A[i]:
                ans[i] = A[i]
        elif tmp % 2 == 1:
            ans[i] = 1
print(sum(ans))
print(*[i + 1 for i in range(n) if ans[i] == 1])
