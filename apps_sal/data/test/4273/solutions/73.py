n = int(input())
li = [0] * 5
for k in range(n):
    s = input()
    if s[0] == 'M':
        li[0] += 1
    elif s[0] == 'A':
        li[1] += 1
    elif s[0] == 'R':
        li[2] += 1
    elif s[0] == 'C':
        li[3] += 1
    elif s[0] == 'H':
        li[4] += 1
ans = 0
for i in range(2 ** 5):
    num = 1
    if str(bin(i)).count('1') == 3:
        for j in range(5):
            if i >> j & 1 == 1:
                num *= li[j]
        else:
            ans += num
print(ans)
