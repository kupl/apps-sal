(h, w) = map(int, input().split())
a = []
data = [0] * w
for i in range(h):
    a_ = input()
    if a_ != '.' * w:
        a.append(a_)
        for j in range(w):
            if a_[j] == '.':
                data[j] += 1
n = len(a)
for i in range(n):
    ans = []
    for j in range(w):
        if data[j] != n:
            ans.append(a[i][j])
    print(*ans, sep='')
