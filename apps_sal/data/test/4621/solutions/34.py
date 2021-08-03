h, w = map(int, input().split())
c = [input() for i in range(h)]
for i in range(h):
    print(c[i] + '\n' + c[i])
