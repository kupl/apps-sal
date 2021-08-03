input()
s, t = input().split()

l = [c1 + c2 for c1, c2 in zip(s, t)]
print(''.join(l))
