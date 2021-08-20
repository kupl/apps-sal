(l, r) = list(map(int, input().split()))
ans = 0
for i in range(100):
    for j in range(100):
        if 2 ** i * 3 ** j > 2000000000:
            break
        if l <= 2 ** i * 3 ** j:
            if r >= 2 ** i * 3 ** j:
                ans = ans + 1
print(ans)
