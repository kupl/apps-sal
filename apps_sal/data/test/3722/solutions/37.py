N = int(input())
AA, AB, BA, BB = [input() == "A" for _ in range(4)]
MOD = 10 ** 9 + 7

if AB:
    AB = not AB
    BA = not BA
    AA, BB = not BB, not AA

if N <= 3:
    ans = 1
elif BB == False:
    ans = 1
elif BA == True:
    ans = pow(2, N - 3, MOD)
else:
    a, b = 1, 0
    for i in range(N - 1):
        a, b = b, (a + b) % MOD
    ans = b

print(ans)
