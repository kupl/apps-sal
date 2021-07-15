f, i, t = [int(x) for x in input().split()]
s = [0] * i 
for kitten in range(f):
    l = input()
    for o in range(i):
        if l[o] == 'Y':
            s[o]+=1
print(sum([1 for x in s if x >= t]))

