N = int(input())
s = [0] * N

for i in range(N):
    s[i] = input()


d = set()
for v in s:
    d.add(v)

print((len(d)))


