s = input()
wcount = 0
for i in range(len(s)-1):
    if s[i+1] == "v" and s[i] == "v":
        wcount += 1

ans = 0
wcountl = 0
for i in range(len(s)-1):
    if s[i+1] == "v" and s[i] == "v":
        wcountl += 1
        wcount -= 1
    elif s[i+1] == "o":
        ans += wcountl*wcount

print(ans)

