s = input()
fav = 753
ans = 1000000.0
for i in range(len(s) - 2):
    num = int(s[i:i + 3])
    ans = min(ans, abs(num - fav))
print(ans)
