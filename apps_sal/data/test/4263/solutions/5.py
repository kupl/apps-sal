s = input()
data = ['A','T','G','C']
ans = 0
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[j] not in data:
            ans = max(ans,j-i)
            break
        elif j == len(s) - 1:
            ans = max(ans,len(s) - i)
print(ans)
