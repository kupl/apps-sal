n = int(input())
s = input()
from itertools import product

for v in product([1,0], repeat=2):
    v = list(v)
    for i in range(n-2):
        if v[i+1]:
            if s[i+1] == 'o':
                v.append(v[i])
            else:
                v.append(int(not v[i]))
        else:
            if s[i+1] == 'o':
                v.append(int(not v[i]))
            else:
                v.append(v[i])
    ans = [0,0]
    for i in range(-1,1):
        if v[i]:
            if s[i] == 'o':
                if v[i-1] == v[i+1]:
                    ans[i+1] = 1
                else:
                    ans[i+1] = 0
            else:
                if v[i-1] != v[i+1]:
                    ans[i+1] = 1
                else:
                    ans[i+1] = 0
        else:
            if s[i] == 'o':
                if v[i-1] == v[i+1]:
                    ans[i+1] = 0
                else:
                    ans[i+1] = 1
            else:
                if v[i-1] != v[i+1]:
                    ans[i+1] = 0
                else:
                    ans[i+1] = 1
    if ans[0] and ans[1]:
        for i in range(n):
            if v[i]:
                v[i] = 'S'
            else:
                v[i] = 'W'
        print((''.join(v)))
        return
print((-1))



