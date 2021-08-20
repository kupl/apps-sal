tgt = 2048 .bit_length() - 1
for _ in range(int(input())):
    n = int(input())
    c = [0] * 31
    for x in input().split():
        c[int(x).bit_length() - 1] += 1
    for i in range(tgt):
        c[i + 1] += c[i] // 2
    print('YES' if c[tgt] else 'NO')
