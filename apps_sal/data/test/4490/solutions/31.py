b = input()

s0 = ['A', 'T', 'C', 'G']
s1 = ['T', 'A', 'G', 'C']

for i, s in enumerate(s0):
    if s == b:
        print((s1[i]))
        break
