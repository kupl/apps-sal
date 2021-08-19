(n, a, b, c) = list(map(int, input().split()))
s = [list(input()) for _ in range(n)]
s.append(['A', 'B'])
d = {'A': a, 'B': b, 'C': c}
ans = []


def calc(add, sub):
    d[add] += 1
    d[sub] -= 1
    ans.append(add)


for (i, [j, k]) in enumerate(s):
    if i == n:
        print('Yes')
        print('\n'.join(ans))
        break
    if d[j] == 0 and d[k] == 0:
        print('No')
        break
    elif j == 'A' and k == 'B':
        if d[j] < d[k]:
            calc(j, k)
        elif d[j] > d[k]:
            calc(k, j)
        elif s[i + 1][0] == 'A':
            calc(j, k)
        else:
            calc(k, j)
    elif j == 'A' and k == 'C':
        if d[j] < d[k]:
            calc(j, k)
        elif d[j] > d[k]:
            calc(k, j)
        elif s[i + 1][0] == 'A':
            calc(j, k)
        else:
            calc(k, j)
    elif j == 'B' and k == 'C':
        if d[j] < d[k]:
            calc(j, k)
        elif d[j] > d[k]:
            calc(k, j)
        elif s[i + 1][0] == 'A' and s[i + 1][1] == 'C':
            calc(k, j)
        else:
            calc(j, k)
