(w, a, b) = list(map(int, input().split()))
if a <= b <= a + w or b <= a <= b + w:
    ans = 0
elif a < b:
    ans = b - a - w
else:
    ans = a - b - w
print(ans)
