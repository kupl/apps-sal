(f, i, t) = list(map(int, input().split()))
q = [0 for x in range(i)]
for g in range(f):
    s = input()
    for j in range(i):
        q[j] += s[j] == 'Y'
kitten = sum([x >= t for x in q])
print(kitten)
