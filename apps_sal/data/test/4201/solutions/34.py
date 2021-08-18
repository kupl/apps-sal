h, w, k = map(int, input().split())
m = [list(input()) for i in range(h)]
o = 0
for h_bit in range(2**h):
    for w_bit in range(2**w):
        c = 0
        for i in range(h):
            for j in range(w):
                if (h_bit >> i) & 1 == 0 and (w_bit >> j) & 1 == 0 and m[i][j] == '
                c += 1
        if c == k:
            o += 1
print(o)
