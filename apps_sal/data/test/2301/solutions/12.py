import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))
A.sort()
Ans = [None]*N
A1 = A[:(N-1)//2][::-1]
A2 = A[(N-1)//2:]
for i in range((N-1)//2):
    Ans[2*i+1] = A1[i]
for i in range(N):
    if Ans[i] is None:
        Ans[i] = A2.pop()
ans = 0
for i in range(1, N-1):
    if Ans[i-1] > Ans[i] and Ans[i] < Ans[i+1]:
        ans += 1
print(ans)
print(*Ans)

