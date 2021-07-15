s = input()
ans = 'None'
for i in range(97, 123):
    if chr(i) not in s:
        ans = chr(i)
        break
print(ans)
