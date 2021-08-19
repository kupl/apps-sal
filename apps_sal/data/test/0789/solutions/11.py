n = input()
ans = 0
for i in range(len(n)):
    ans *= 2
    ans += 1
    if n[i] == '7':
        ans += 1
print(ans)
