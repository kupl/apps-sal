(w, h) = list(map(int, input().split()))
a = []
for i in range(h):
    a.append(input())
for i in range(w):
    line = ''
    for j in range(h):
        line += a[j][i] * 2
    print(line, line, sep='\n')
