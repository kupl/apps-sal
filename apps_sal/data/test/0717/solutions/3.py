n = int(input())
s, d = list(map(int, input().split()))
last = s
for i in range(n - 1):
    s, d = list(map(int, input().split()))
    c = max(0, last - s)
    c = (c + d) // d
    new = c * d + s
    if new - d >= last:
        new -= d
    if new <= last:
        new += d
    last = new
print(last)
