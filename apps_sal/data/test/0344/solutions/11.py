arr = ['a', 'e', 'i', 'o', 'u']
ans = True
s = input()
n = len(s)
for i in range(n):
    if(s[i] not in arr and i < n - 1):
        if(s[i] == 'n'):
            continue
        else:
            if(s[i + 1] not in arr):
                ans = False
                break
    if(s[i] not in arr and i == n - 1):
        if(s[i] != 'n'):
            ans = False
            break
if(ans == True):
    print("YES")
else:
    print("NO")
