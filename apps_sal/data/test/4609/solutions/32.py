N = int(input())
A = [int(input()) for _ in range(N)]
dic = {num: 0 for num in set(A)}
for i in range(N):
    dic[A[i]] = 1 if dic[A[i]] == 0 else 0
ans = 0
for num in set(A):
    ans += dic[num]
print(ans)
