s = input()
ans = 999
for i in range(0, len(s) - 2):
    if ans > abs(int(s[i:i + 3]) - 753):
        ans = abs(int(s[i:i + 3]) - 753)
print(ans)
