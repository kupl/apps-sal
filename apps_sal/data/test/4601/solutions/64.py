n, k = map(int, input().split())
h = sorted(list(map(int, input().split())))
if k >= len(h):
    print(0)
    return
print(sum(h[0:n - k]))
