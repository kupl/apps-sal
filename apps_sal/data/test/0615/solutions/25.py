N = int(input())
A = list(map(int, input().split()))
s = 0
AS = []
for i in range(N):
    s += A[i]
    AS.append(s)
Ans = AS[N - 1] + 1
L = 0
R = 2
for Mid in range(1, N - 2):
    Sum_L = AS[Mid]
    Sum_R = AS[N - 1] - Sum_L
    while abs(Sum_L - 2 * AS[L]) > abs(Sum_L - 2 * AS[L + 1]):
        L += 1

    while R <= N - 3 and abs(AS[N - 1] - 2 * AS[R] + AS[Mid]) > abs(AS[N - 1] - 2 * AS[R + 1] + AS[Mid]):
        R += 1
    P = AS[L]
    Q = AS[Mid] - AS[L]
    S = AS[R] - AS[Mid]
    T = AS[N - 1] - AS[R]
    Ans = min(Ans, abs(max(P, Q, S, T) - min(P, Q, S, T)))
print(Ans)
