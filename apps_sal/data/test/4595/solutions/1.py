s = input()
start = len(s)
end = 0
ans = 0

for i in range(len(s)):
    if s[i] == 'A':
        start = min(start , i)
    if s[i] == 'Z':
        end = max(end, i)
    ans = end - start + 1
print(ans)
