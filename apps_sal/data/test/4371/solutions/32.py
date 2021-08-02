s = input()
ans = abs(753 - int(s[0] + s[1] + s[2]))
for i in range(1, len(s) - 2):
    n = s[i] + s[i + 1] + s[i + 2]
    ans = min(ans, abs(int(n) - 753))
print(ans)
