s = input()
#s = "5"
n = int(s)

s = input()
#s = "RBBRR"
x = s

ans = 0
for i in range(0, n):
    if x[i] == 'B':
        ans += 1 << i

print(ans)
