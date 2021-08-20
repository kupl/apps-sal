(n, k) = list(map(int, input().split()))
x = list(map(int, input().split()))
l = r = ln = 0
while r < n:
    if r > 0 and x[r] == x[r - 1]:
        l = r
    ln = max(ln, r - l + 1)
    r += 1
print(ln)
