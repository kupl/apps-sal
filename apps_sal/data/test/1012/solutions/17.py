t = int(input())
for i in range(t):
    s = input()
    r = ''.join(sorted(list(s)))
    if r[0] == r[-1]:
        print(-1)
    else:
        print(r)


