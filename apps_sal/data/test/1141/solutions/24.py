_, m = [int(x) for x in input().split()]

s = list(input())

for ii in range(m):
    args = input().split()
    l, r = int(args[0]), int(args[1])
    c1, c2 = args[2], args[3]

    for j in range(l - 1, r):
        if s[j] == c1:
            s[j] = c2

print(''.join(s))


