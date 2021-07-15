def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n = ii()
s = input().strip()
t = []
v = 'aeiouy'
i = 0
while i < n:
    t += [s[i]]
    if s[i] not in v:
        i += 1
        continue
    j = i + 1
    while j < n and s[j] in v:
        j += 1
    i = j
print(''.join(t))
