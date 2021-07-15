import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

start = [0]*M
end = [0]*M
S = [0]*M
a = 0
score = 0
total = 0
for i in range(N-1):
    p, q = A[i]-1, A[i+1]-1
    start[q] += 1
    end[p] += 1
    S[q] += (q-p-1+M)%M
    total += (q-p+M)%M
    score += max(0, (q-p-1+M)%M - q)
    if p > q:
        a += 1

ans = total - score
ind = M-1
for _ in range(4*M):
    a -= end[ind]
    score += S[ind] - a
    a += start[ind]
    ind -= 1
    if ind < -M: ind += M
    ans = min(ans, total-score)
print(ans)
