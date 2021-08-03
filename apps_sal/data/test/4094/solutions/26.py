k = int(input())

if k % 2 == 0 or k % 5 == 0:
    print(-1)
    return

ans = 1
num = 7
while num % k != 0:
    num = 10 * num + 7
    num %= k
    ans += 1

print(ans)
