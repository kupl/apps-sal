import itertools
n = int(input())
name = [0] * 5
s = []
for i in range(n):
    st = input()
    if st[0] == 'M':
        name[0] += 1
    elif st[0] == 'A':
        name[1] += 1
    elif st[0] == 'R':
        name[2] += 1
    elif st[0] == 'C':
        name[3] += 1
    elif st[0] == 'H':
        name[4] += 1
    s.append(st)

ans = 0
for v in itertools.combinations(name, 3):
    # print(v)
    ans += v[0] * v[1] * v[2]

print(ans)
