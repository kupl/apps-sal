n, k = map(int, input().split())
x = list(map(int, input().split()))
li = []
for i in range(n - k + 1):
    li += [x[k - 1 + i] - x[i] + min(abs(x[k - 1 + i]), abs(x[i]))]
print(min(li))
