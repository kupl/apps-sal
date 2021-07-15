s=input()
ans = 653
for i in range(len(s)-2):
    x = abs(753 - int(s[i:i+3]))
    ans = min(ans,x)
print(ans)
