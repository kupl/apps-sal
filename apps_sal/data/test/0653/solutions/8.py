n = int(input())
ans = [0] * 10
s = input()
for i in range(len(s)):
    if s[i] == 'L':
        f = 0
        while ans[f] != 0:
            f += 1
        ans[f] = 1
    elif s[i] == 'R':
        f = 9
        while ans[f] != 0:
            f -= 1
        ans[f] = 1
    else:
        ans[int(s[i])] = 0
for i in range(10):
    print(ans[i], end='')
