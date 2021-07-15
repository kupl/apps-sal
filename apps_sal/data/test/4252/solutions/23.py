n = int(input())
s = input()
p = str()
ans = 0
for i in range(n-2):
    if s[i] == "x" and s[i+1] == "x" and s[i+2] == "x":
        ans += 1

print(ans)
