N, K= list(map(int, input().split()))
Rcnt = N * 2
Gcnt = N * 5
Bcnt = N * 8

res = (Rcnt + K - 1) // K + (Gcnt + K - 1) //K + (Bcnt + K -1 ) // K
print(res)

