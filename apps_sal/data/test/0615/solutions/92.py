#102_D
N = int(input())
A = [int(i) for i in input().split()]
s = 0
AS = []
for i in range(N):
    s += A[i]
    AS.append(s)
#尺取り法
Ans = AS[N-1]+1
L = 0
R = 2
for Mid in range(1, N-2):
    Sum_L = AS[Mid]
    Sum_R = AS[N-1]-Sum_L
    while abs((Sum_L - AS[L]) - AS[L]) > abs((Sum_L - AS[L+1]) - AS[L+1]):
        L += 1

    while abs((AS[N-1]-AS[R]) - (AS[R]-Sum_L)) > abs((AS[N-1]-AS[R+1]) - (AS[R+1]-Sum_L)):
        R += 1
    P = AS[L]
    Q = Sum_L-AS[L]
    S = AS[R]-Sum_L
    T = AS[N-1]-AS[R]
    #print(Mid,L,R,abs(max(P,Q,S,T)-min(P,Q,S,T)))
    Ans = min(Ans, abs(max(P, Q, S, T)-min(P, Q, S, T)))
print(Ans)

