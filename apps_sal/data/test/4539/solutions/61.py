n = input()
ans = 0
for i in range(len(n)):
    ans += int(n[i])
if int(n) % ans == 0:
    print('Yes')
else:
    print('No')
