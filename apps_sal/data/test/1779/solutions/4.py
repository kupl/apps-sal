a = input()
b = input()
A = a.upper()
B = b.upper()

d = dict(zip(list(a + A), list(b + B)))

s = list(input())

ans = list(map(lambda x : d[x] if x in d else x, s))

print(''.join(ans))
