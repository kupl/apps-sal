n, k = map(int, input().split())
A = list(map(int, input().split()))
last = A[0]
# print(last);
#last = 0;
cnt = 0
f = 0
for q in range(n - 1):
    #print(A[q + 1], last, k);
    if A[q + 1] - last > k:
        if A[q] == last:
            f = 1
            break
        last = A[q]
        cnt = cnt + 1
    if A[q + 1] - last > k:
        f = 1
        break
if not f:
    print(cnt + 1)
else:
    print(-1)
