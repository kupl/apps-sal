def f_frog_jump(N, S):
    ans = 0
    for c in range(1, N):
        current_ans, k = 0, 1
        while k * c < N - 1:
            a = N - 1 - k * c
            b = a - c
            if not (a <= b or b <= 0 or (a % c == 0 and a <= k * c)):
                current_ans += S[N - 1 - k * c] + S[k * c]
                ans = max(ans, current_ans)
            k += 1
    return ans


N = int(input())
S = [int(i) for i in input().split()]
print(f_frog_jump(N, S))
