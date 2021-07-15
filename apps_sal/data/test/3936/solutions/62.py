MOD = 10 ** 9 + 7
N = int(input())
s1 = input()
s2 = input()
index = 0
ans = 0
tmp = 0
if N == 1:
    print(3)
    return

if s1[index] == s1[index + 1]:
    ans = 6
    tmp = 6
    index += 2
else:
    ans = 3
    tmp = 3
    index += 1
while index < N:
    if tmp == 3:
        if s1[index] == s2[index]:
            index += 1
            tmp = 3
            ans *= 2 % MOD
        else:
            index += 2
            ans *= 2 % MOD
            tmp = 6
    else:
        if s1[index] == s2[index]:
            index += 1
            tmp = 3
        else:
            index += 2
            tmp = 6
            ans *= 3 % MOD

print(ans % MOD)
