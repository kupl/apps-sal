from itertools import product
n = int(input())
s = input()

for v in product([1, 0], repeat=2):
    v = list(v)
    for i in range(n - 2):
        if v[i + 1]:
            if s[i + 1] == 'o':
                v.append(v[i])
            else:
                v.append(not v[i])
        else:
            if s[i + 1] == 'o':
                v.append(not v[i])
            else:
                v.append(v[i])
    ans = [0, 0]
    for i in range(-1, 1):
        if v[i]:
            if s[i] == 'o':
                if v[i - 1] == v[i + 1]:
                    ans[i + 1] = 1
                else:
                    ans[i + 1] = 0
            else:
                if v[i - 1] == v[i + 1]:
                    ans[i + 1] = 0
                else:
                    ans[i + 1] = 1
        else:
            if s[i] == 'o':
                if v[i - 1] == v[i + 1]:
                    ans[i + 1] = 0
                else:
                    ans[i + 1] = 1
            else:
                if v[i - 1] == v[i + 1]:
                    ans[i + 1] = 1
                else:
                    ans[i + 1] = 0
    if ans[0] and ans[1]:
        print(''.join(['S' if x == 1 else 'W' for x in v]))
        return
print(-1)
