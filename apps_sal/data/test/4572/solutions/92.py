s = input()
s = list(s)
s = set(s)
l = [chr(ord("a") + i) for i in range(26)]
ans = 'None'
for i in l:
    if i not in s:
        ans = i
        break
print(ans)
