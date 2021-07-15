s = input()
n = len(s)
s = s+"0"

ans1,ans2 = -1,-1

for i in range(n-1):
    if s[i] == s[i+1]:
        ans1,ans2 = i+1,i+2
        break

    if s[i] == s[i+2]:
        ans1,ans2 = i+1,i+3
        break

print(ans1,ans2)
