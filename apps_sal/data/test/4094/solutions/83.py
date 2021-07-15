K = int(input())

MOD = 7%K
if MOD == 0:
    print(1)
    return

for i in range(2, K+1):
    MOD = (MOD * 10 + 7) % K
    if MOD == 0:
        print(i)
        return

print(-1)
