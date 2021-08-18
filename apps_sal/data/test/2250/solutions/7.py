t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())

    ans = 0
    if len(set(s)) != 1:
        ind = 0
        for i in range(1, n):
            if s[i] != s[i - 1]:
                ind = i
                break
        S = s[ind:] + s[:ind]
        A = [1]
        for i in range(1, n):
            if S[i] != S[i - 1]:
                A.append(1)
            else:
                A[-1] += 1
        for i in range(len(A)):
            ans += A[i] // 3

    else:
        ans = 1
        n -= 1

        ans += n // 3
    print(ans)
