w, m = map(int, input().split())
for i in range(33):
    m = min(m, abs(w**(32 - i) - m))
print("NO" if m else "YES")
