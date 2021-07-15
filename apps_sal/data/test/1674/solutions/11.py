def sumn(l, r):
    nonlocal dmgs
    tmp = []
    for i in range(l, r + 1):
        tmp.append(dmgs[i])
    tmp.sort(reverse=True)
    return sum(tmp[:k])
    

n, k = map(int, input().split())
dmgs = [int(x) for x in input().split()]
s = input()
d = {}
key = 'abcdefghijklnmopqrstuvwxyz'
l = 0
r = 0
total = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        r = i
        total += sumn(l, r)
        l = i + 1
total += sumn(l, n - 1)
print(total)
