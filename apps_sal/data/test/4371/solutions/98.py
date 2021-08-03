s = input()

ans = 1000
for i in range(len(s) - 2):
    diff = abs(int(s[i:i + 3]) - 753)
    if diff < ans:
        ans = diff

print(ans)
