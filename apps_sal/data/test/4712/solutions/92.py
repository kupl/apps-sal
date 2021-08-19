h, w = map(int, input().split())
al = []
for _ in range(h):
    row = input()
    row = '#' + row + '#'
    al.append(row)

top = '#' * (w + 2)
print(top)
for a in al:
    print(a)
print(top)
