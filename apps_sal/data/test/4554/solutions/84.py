(w, a, b) = map(int, input().split())
aw = a + w
bw = b + w
print(max(0, a - bw, b - aw))
