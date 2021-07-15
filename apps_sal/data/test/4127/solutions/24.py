a, B = input().split()
a = int(a)
i = 2
ans = 0
for b in B:
    if b == ".":
        continue
    ans += int(b) * a * 10 ** i
    i -= 1
print((ans // 100))

