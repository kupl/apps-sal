(N, K) = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
ans = 0
for i in range(1, int(S ** 0.5) + 1):
    if S % i != 0:
        continue
    for j in range(2):
        d = i if j else S // i
        B = sorted(map(lambda a: a % d, A))
        C = [0]
        for k in range(N):
            C.append(C[-1] + B[k])
        for k in range(N + 1):
            if ((N - k) * d - (C[-1] - C[k]) - C[k]) % d == 0:
                if max(C[k], (N - k) * d - (C[-1] - C[k])) <= K:
                    ans = max(ans, d)
print(ans)
