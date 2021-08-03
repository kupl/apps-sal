def I(): return int(input())


N = I()
ans = 0
if N >= 105:
    for i in range(105, N + 1, 2):
        count_yakusuu = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                count_yakusuu += 2
        if count_yakusuu == 8:
            ans += 1
print(ans)
