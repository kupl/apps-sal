h, w = map(int, input().split())
a = ['#' * (w + 2)]
for i in range(h):
    a.append('#' + input() + '#')
a += ['#' * (w + 2)]

for i in range(h + 2):
    print(a[i])
