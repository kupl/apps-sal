c = input()
d = 'AGTC'
for i in range(0, 4):
    if d[i] == c:
        print(d[(i + 2) % 4])
