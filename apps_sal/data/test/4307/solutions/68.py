def divisor(n):
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            cnt += 1
    return cnt*2


n = int(input())
ans = 0
for i in range(1, n+1):
    if i%2 != 0 and divisor(i) == 8:
        ans += 1
print(ans)

