N = int(input())
b = []
for i in range(6):
    (N, r) = divmod(N, 2)
    b.append(r)
ans = 0
if b[0]:
    ans += 16
if b[1]:
    ans += 2
if b[2]:
    ans += 8
if b[3]:
    ans += 4
if b[4]:
    ans += 1
if b[5]:
    ans += 32
print(ans)
