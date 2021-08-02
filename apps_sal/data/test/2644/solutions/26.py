n = int(input())
p = list(map(int, input().split()))

ans, tmp, res = [], [], []
for i in range(n):
    if i != 0:
        tmp.append(i)
    if p[i] - 1 == len(ans):
        res += [p[i]] + p[len(ans):i - 1]
        ans += tmp[::-1]
        tmp = []
        p[i] = p[i - 1]
else:
    res += [p[i]] + p[len(ans):i - 1]
    ans += tmp[::-1]
print(*(ans if res == [i + 1 for i in range(n)] else[-1]), sep='\n')
