n = int(input())
k = [0] * 5  # M-A-R-C-H
for _ in range(n):
    s = input()[0]
    if s == "M":
        k[0] += 1
    elif s == "A":
        k[1] += 1
    elif s == "R":
        k[2] += 1
    elif s == "C":
        k[3] += 1
    elif s == "H":
        k[4] += 1
ans = 0
for i in range(32):
    bit = bin(i)[2:].zfill(5)
    if bit.count("1") != 3:
        continue
    count = 1
    for j in range(5):
        if bit[j] == "1":
            count *= k[j]
    ans += count
print(ans)
