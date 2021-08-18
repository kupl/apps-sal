n, k = map(int, input().split())
h = list(map(int, input().split()))
ans = [0] * (n - k + 1)
ans[0] = sum(h[:k])
minim = ans[0]
aminim = 0
for i in range(1, n - k + 1):
    ans[i] = ans[i - 1] + h[i + k - 1] - h[i - 1]
    if ans[i] < minim:
        minim = ans[i]
        aminim = i
print(aminim + 1)
