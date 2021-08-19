(w, a, b) = map(int, input().split())
if abs(a - b) < w:
    ans = 0
else:
    ans = abs(a - b) - w
print(ans)
