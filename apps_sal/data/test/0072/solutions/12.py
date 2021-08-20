N = int(input())
n = [0, 0, 0]
for i in range(3):
    z = [0 for i in range(128)]
    x = input()
    for j in x:
        z[ord(j)] += 1
    n[i] = min(N + max(z), len(x) - 1 if N == 1 and len(x) == max(z) else len(x))
r = max(n)
if n.count(r) == 1:
    if n[0] == r:
        print('Kuro')
    elif n[1] == r:
        print('Shiro')
    else:
        print('Katie')
else:
    print('Draw')
