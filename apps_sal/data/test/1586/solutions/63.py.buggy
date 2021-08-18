n = int(input())
if n % 2 == 1:
    print(0)
    return
n //= 2
t = 1
count = -1
while n >= t:
    t *= 5
    count += 1
ans = 0
for i in range(1, count + 1):
    ans += n // (5**i)
print(ans)
