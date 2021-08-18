
n = 0
m = 0
MOD = 0
cap = [0] * 505
ans = [[-1] * 505 for i in range(505)]


def f(one, two):
    if one == 0 and two == 0:
        return 1

    if two > len(ans[one]):
        print(str(one) + ' ' + str(two) + ' ' + len(ans[one]))
    if ans[one][two] != -1:
        return ans[one][two]

    temp = 0
    if two > 1:
        x = two * (two - 1) / 2 * f(one + 2, two - 2)
        temp += x % MOD
    if one > 1:
        x = one * (one - 1) / 2 * f(one - 2, two)
        temp += x % MOD
    if two > 0 and one > 0:
        x = one * two * f(one, two - 1)
        temp += x % MOD
    temp = temp % MOD
    ans[one][two] = temp
    return temp


temp = input().split(' ')
n = int(temp[0])
m = int(temp[1])
MOD = int(temp[2])
for i in range(0, m):
    cur = ''
    cur = input()
    for j in range(0, n):
        if cur[j] == '1':
            cap[j] += 1

n_one = 0
n_two = 0
for i in range(0, n):
    if cap[i] == 0:
        n_two += 1
    if cap[i] == 1:
        n_one += 1

print(int(f(n_one, n_two)))
