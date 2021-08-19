(w, a, b) = list(map(int, input().split()))
ans = abs(a - b) - w
print(ans) if ans > 0 else print(0)
