c = [chr(i) for i in range(97, 97+26)]
s = input()
ans = 'None'
for i in c:
    if i not in s:
        ans = i
        break
print(ans)
