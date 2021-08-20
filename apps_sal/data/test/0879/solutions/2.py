n = int(input().strip())
route = list(map(int, input().strip().split()))
out = [n]
i = n - 2
while i >= 0:
    out.append(route[i])
    i = route[i] - 2
print(' '.join(map(str, reversed(out))))
