n = int(input())
w = list(map(int, input().split()))
result = sum(w)
for i in range(n):
    wk = abs(sum(w[:i]) - sum(w[i:]))
    if result > wk:
        result = wk
print(result)
