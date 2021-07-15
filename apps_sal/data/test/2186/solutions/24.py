n,m = [int(i) for i in input().split()]
memory = set()
d = 31918781974729
ans = [None] * m

def Hash(x):
    t = 0
    mul = 1
    for char in x:
        t = (t + ord(char) * mul) % d
        mul = (mul * 2193) % d
    return t

for i in range(n):
    string = input()
    t = Hash(string)
    mul = 1
    for j in range(len(string)):
        for char in 'abc':
            if string[j] != char:
                memory.add((t + (ord(char) - ord(string[j])) * mul) % d)
        mul = (mul * 2193) % d
for i in range(m):
    string = input()
    t = Hash(string)
    if t in memory:
        ans[i] = 'YES'
    else:
        ans[i] = 'NO'
print(*ans, sep = '\n')

