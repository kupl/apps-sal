n, m, l = list(map(int, input().split()))

a = list(map(int, input().split()))

cuts = 0
prev = False
for i in range(n):
    if a[i] > l:
        if prev:
            continue
        else:
            cuts += 1
            prev = True
    else:
        prev = False

for _ in range(m):
    s = input()
    if s.startswith('0'):
        print(cuts)
    else:
        p, d = list(map(int, s[1:].split()))
        p -= 1
        if a[p] <= l and a[p] + d > l:
            t = (p - 1 in range(n) and a[p - 1] > l) + \
                (p + 1 in range(n) and a[p + 1] > l)
            if t == 0:
                cuts += 1
            elif t == 1:
                pass
            else:
                cuts -= 1
        a[p] += d

'''

4 7 3
4 2 3 1
0
1 2 3
0
1 1 3
0
1 3 1
0


'''
