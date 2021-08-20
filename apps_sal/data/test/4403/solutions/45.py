word = input()
ans = 0
for i in word:
    if i == '+':
        ans += 1
    else:
        ans -= 1
print(ans)
