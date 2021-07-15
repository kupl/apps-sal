s = input()
begin = 0
end = 0
for i in range(len(s)):
    if s[i]=='A':
        begin = i
        break
for i in range(len(s)-1,-1,-1):
    if s[i]=='Z':
        end = i
        break
print(end-begin+1)
