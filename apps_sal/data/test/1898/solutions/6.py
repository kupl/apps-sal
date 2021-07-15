n = int(input())
hate = 'I hate that '
love = 'I love that '
ans = ''
for i in range(1, n):
    if i%2 == 0: ans += love
    else: ans += hate
if n%2 == 0: ans += 'I love it'
else: ans += 'I hate it'
print(ans)

