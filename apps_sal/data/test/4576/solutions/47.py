A = int(input())
B = int(input())
C = int(input())
X = int(input())
ans = 0
for a in range(0, A + 1):
    if 500 * a > X:
        continue
    for b in range(0, B + 1):
        if 500 * a + 100 * b > X:
            continue
        for c in range(0, C + 1):
            if 500 * a + 100 * b + 50 * c == X:
                ans += 1
print(ans)
