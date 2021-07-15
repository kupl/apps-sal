s = input()
n = len(s)

ans = 'Yes'

for i in range(n):
    if i%2 == 0 and s[i] == 'L': ans = 'No'
    if i%2 != 0 and s[i] == 'R': ans = 'No'

print(ans)
