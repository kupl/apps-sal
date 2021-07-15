n, m, x, y = list(map(int, input().split()))

p = list(map(int, input().split()))
q = list(map(int, input().split()))

if max(max(p), x) < min(min(q), y):
    print("No War")
else:
    print("War")
