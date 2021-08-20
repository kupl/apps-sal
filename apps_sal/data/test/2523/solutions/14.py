s = input()
half = (len(s) - 1) // 2
ans = half + 1
c = s[half]
for (x, y) in zip(s[half + 1:], s[half - (len(s) % 2 == 1)::-1]):
    if x == c and y == c:
        ans += 1
    else:
        break
print(ans)
