n = int(input())
for i in range(n):
    st = input()
    ans = []
    c = 1
    for j in range(1, len(st)):
        if st[j] == st[j - 1]:
            c += 1
        else:
            if c % 2 == 1:
                if not st[j - 1] in ans:
                    ans.append(st[j - 1])
            c = 1
    if c % 2 == 1:
        if not st[len(st) - 1] in ans:
            ans.append(st[len(st) - 1])
    ans.sort()
    for f in ans:
        print(f, end='')
    print()

