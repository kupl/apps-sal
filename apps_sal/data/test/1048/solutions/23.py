n = int(input())

cs = input()

cc = {'U': 0, 'D': 0, 'L': 0, 'R': 0}

for c in cs:
    cc[c] += 1


total = n - abs(cc['U'] - cc['D']) - abs(cc['L'] - cc['R'])
print(total)
