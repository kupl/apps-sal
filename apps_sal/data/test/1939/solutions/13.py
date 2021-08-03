n, k = list(map(int, input().split()))
for i in range(n):
    out = ''
    for j in range(n):
        if i == j:
            out += str(k) + ' '
        else:
            out += str(0) + ' '
    print(out.rstrip())
