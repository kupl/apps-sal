n = int(input())
s = input()

count = s.count('E')
ans = s.count('E')
for i in range(len(s)):
    if s[i] == 'E':
        count -=1
    else:
        count+=1
    ans = min(count,ans)
print(ans)
