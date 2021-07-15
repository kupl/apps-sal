n, k = map(int, input().split())
x = list(map(int, input().split()))
ans = []
for j in range(n-k+1):
    if x[j] > 0:
        ans.append(x[j+k-1])
    elif x[j] <= 0 <= x[j+k-1]:
        ans.append(min(2*abs(x[j])+x[j+k-1], abs(x[j])+2*x[j+k-1]))
    else:
        ans.append(-x[j])
print(min(ans))
