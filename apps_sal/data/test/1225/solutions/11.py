H = int(input())
count = 0
while H != 1:
    H //= 2
    count += 1
ans = 0
for i in range(count +1):
    ans += 2 ** i
print(ans)

