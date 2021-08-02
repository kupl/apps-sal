n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
st = 0
end = 0
res = 1
for i in range(1, n):
    if a[i] != a[i - 1]:
        end += 1
    else:
        res = max(res, end - st + 1)
        st = i
        end = i
if end == n - 1:
    res = max(res, end - st + 1)
print(res)
