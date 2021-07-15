x = int(input())

ans = x
past = int(ans**0.5)
divisor = [i for i in range(1, past+1, 1) if x%i == 0]
while len(divisor) != 1:
    if ans%2 == 0:
        ans += 1
    else:
        ans += 2
    root = int(ans**0.5)
    divisor = [j for j in range(1, root+1, 1) if ans%j == 0]

print(ans)
