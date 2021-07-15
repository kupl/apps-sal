N = int(input())

if N % 2 == 1:
    print(0)
    return

n = 10
ans = 0
while True:
    if n > N:
        break
    ans += N//n
    n *= 5

print(ans)
