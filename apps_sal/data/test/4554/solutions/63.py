w, a, b = list(map(int, input().split()))
res = max(0, abs(a - b) - w)
print(res)
