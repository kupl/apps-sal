s = input()
t = input()
n = len(s)
ans = 0;
for i in range(n):
    if(s[i] != t[i]):
        ans += 1
print(ans)        

