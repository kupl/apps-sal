def read_ints():
    return list(map(int, input().strip().split()))


(n, x) = read_ints()
s = abs(sum(read_ints()))
print((s + x - 1) // x)
