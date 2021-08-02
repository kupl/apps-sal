n, k = list(map(int, input().split()))
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
A.sort(key=lambda x: x[0])
cnt = 0
while k > 0:
    k -= A[cnt][1]
    cnt += 1
print((A[cnt - 1][0]))
