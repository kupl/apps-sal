n, m = list(map(int, input().split()))
pic_a = [input() for _ in range(n)]
pic_b = [input() for _ in range(m)]
top = pic_b[0][0]
if m == 1:
    for line_a in pic_a:
        for chr_a in line_a:
            if top == chr_a:
                print('Yes')
                return
    print('No')
    return
for i, line_a in enumerate(pic_a[:-m + 1]):
    for j, chr_a in enumerate(line_a[:-m + 1]):
        if top == chr_a:
            for k, line_b in enumerate(pic_b):
                if line_b != pic_a[i + k][j:j + m]:
                    break
            else:
                print('Yes')
                return
print('No')
