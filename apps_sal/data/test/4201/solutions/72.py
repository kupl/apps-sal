h, w, k = [int(i) for i in input().split()]
c = [input() for i in range(h)]

cnt = 0
for i in range(1 << h):
    bit_h = [0] * h
    for j in range(h): bit_h[j] = int(i & (1 << j) > 0)
    for j in range(1 << w):
        bit_w = [0] * w
        for l in range(w):
            bit_w[l] = int(j & (1 << l) > 0)
        cnt_t = 0
        for m in range(h):
            for n in range(w):
                if bit_h[m] == 0 and bit_w[n] == 0 and c[m][n] == "#": cnt_t += 1
        if cnt_t == k:
            cnt += 1
            #print(cnt_t)

print(cnt)
