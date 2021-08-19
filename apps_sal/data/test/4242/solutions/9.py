(A, B, K) = list(map(int, input().split()))
ans = []
for a in range(1, A + 1):
    if A % a == 0 and B % a == 0:
        ans.append(a)
print(ans[-K])
