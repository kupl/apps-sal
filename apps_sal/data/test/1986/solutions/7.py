n, k = list(map(int, input().split()))
ans = []
for i in range(n):
    f, t = list(map(int, input().split()))
    if(t > k):
        ans.append(f - t + k)
    else:
        ans.append(f)
print(max(ans))
