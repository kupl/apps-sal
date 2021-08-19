(a, b, k) = list(map(int, input().split()))
lis1 = []
lis2 = []
lis3 = []
for i in range(0, k):
    ap = a + i
    bm = b - i
    lis1.append(ap)
    lis2.append(bm)
lis3 = lis1 + lis2
sorted_lis = sorted(set(lis3))
for ans in sorted_lis:
    if a <= ans and ans <= b:
        print(ans)
