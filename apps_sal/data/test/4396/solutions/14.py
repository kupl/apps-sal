N = int(input())
s = 0
for i in range(N):
    (x, u) = map(str, input().split())
    if u == 'JPY':
        s += int(x)
    else:
        s += 380000.0 * float(x)
print(s)
