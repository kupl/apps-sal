m = 10 ** 9 + 7
t = int(input())
while t:
    t -= 1
    s = input()
    m = int(input())
    b = list(map(int, input().split()))
    fin = sorted(s)
    ans = [''] * m
    while '' in ans:
        new = [index for (index, value) in enumerate(b) if value == 0]
        while fin.count(fin[-1]) < len(new):
            fin = list(filter(lambda x: x != fin[-1], fin))
        for i in new:
            b[i] = -1
            ans[i] = fin[-1]
        fin = list(filter(lambda x: x != fin[-1], fin))
        for i in range(len(b)):
            if b[i] != -1:
                for j in new:
                    b[i] -= abs(i - j)
    print(''.join(ans))
