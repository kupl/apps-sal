N = int(input())
(D, X) = map(int, input().split())
A = [int(input()) for i in range(N)]
cnt = 0
for a in A:
    if D % a == 0:
        cnt += D // a
    else:
        cnt += D // a + 1
print(X + cnt)
