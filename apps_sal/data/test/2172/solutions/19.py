import functools

n,m = (int(x) for x in input().split(" "))

lang = {}

for i in range(0,m):
    a,b = (x for x in input().split(" "))
    if len(a) > len(b) :
        lang[a] = b
    else:
        lang[b] = a

def shorter(x):
    if x in lang:
        return lang[x]
    else:
        return x

print(functools.reduce(lambda x,y: x+" "+y,[shorter(x) for x in input().split()]))



