temp = input().split()
n = int(temp[0])
x = int(temp[1])
temp = input().split()
a = [int(k) for k in temp]

c = [0 for i in range(10**5 + 1)]

for i in range(n):
    c[a[i]] += 1

ans = 0
for i in range(n):
    if a[i] ^ x <= 10**5:
        ans += c[a[i] ^ x]

if x == 0:
    ans -= n

ans = int(ans / 2)

print(ans)
