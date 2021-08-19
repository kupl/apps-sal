MOD = 10 ** 9 + 7
n = int(input())
s1 = input()
s2 = input()
if s1[0] == s2[0]:
    end = 1
    count = 1
    ans = 3
else:
    end = 0
    count = 2
    ans = 6
while count < n:
    if end == 1:
        if s1[count] == s2[count]:
            ans *= 2
            ans %= MOD
            count += 1
        else:
            ans *= 2
            ans %= MOD
            count += 2
            end = 0
    elif s1[count] == s2[count]:
        count += 1
        end = 1
    else:
        ans *= 3
        ans %= MOD
        count += 2
print(ans)
