a = input()
b = input()

def foo(b, i, pos, poss):
    if i == len(b):
        poss.append(pos)
    elif b[i] == '+':
        foo(b,i+1,pos+1, poss)
    elif b[i] == '-':
        foo(b,i+1,pos-1, poss)
    else:
        foo(b,i+1,pos+1, poss)
        foo(b,i+1,pos-1, poss)

pos0 = 0
for x in a:
    if x == '+':
        pos0+=1
    else:
        pos0-=1

q = 0
for x in b:
    if x == '?':
        q+=1

poss = []
res = 0
foo(b, 0, 0, poss)
for x in poss:
    if x == pos0:
        res+=1

print (res / 2 ** q)
