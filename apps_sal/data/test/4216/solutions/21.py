N = int(input())

ans = len(str(N))
for A in range(1, int(-(-N**0.5 // 1)) + 1):
    if N % A != 0:
        continue

    B = N // A
    ans = min(ans, max(len(str(A)), len(str(B))))

print(ans)
