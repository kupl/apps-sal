N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] = (A[i], i + 1)
A.sort()
ans = ''
for tup in A:
    v, i = tup
    ans += str(i) + ' '
print(ans)
