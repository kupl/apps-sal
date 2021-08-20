ans = 0
for (i, c) in enumerate(input()):
    if i % 2 == 0 and c == 'p':
        ans -= 1
    elif i % 2 == 1 and c == 'g':
        ans += 1
print(ans)
