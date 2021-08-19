(n, x) = map(int, input().split())
patty = [1]
barger = [1]
ans = 0
for i in range(n):
    patty.append(2 * patty[-1] + 1)
    barger.append(2 * barger[-1] + 3)
i = n
while x > 0:
    for _ in range(n):
        if x >= barger[i]:
            x -= barger[i]
            ans += patty[i]
            if x > 0:
                ans += 1
                x -= 1
            break
        i -= 1
        x -= 1
print(ans)
