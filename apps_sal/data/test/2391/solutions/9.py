import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

h = 10**11+7
b = 10**7+7

H = [1]
for _ in range(N):
    H.append((H[-1]*b)%h)

allSum = 0
for i in range(N):
    allSum = (allSum + H[i]) % h

ok = [True]*N
ans = [0]*N

C = []
D = []
for i in range(N):
    C.append(A[i-1]^A[i])
    D.append(B[i-1]^B[i])


HashA = 0
for i, a in enumerate(C):
    HashA = (HashA + a*H[i]%h) % h

HashB = 0
for i, a in enumerate(D):
    HashB = (HashB + a*H[i]%h) % h

ans = []
for k in range(N):
    if HashA == HashB:
        ans.append(k)
    HashB = (HashB * b) % h
    HashB = (HashB + (1-H[N])*D[-k-1] % h) % h

for k in ans:
    print(k, A[k]^B[0])
