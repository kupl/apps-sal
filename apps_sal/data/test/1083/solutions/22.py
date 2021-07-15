from collections import Counter
n=int(input())
z=0
for i in range(n+1):
    z=z+i
print(z%2)
z=3
s=1
a={1}
for i in range(3,n+1):
    d=(z+i)//2-s
    if d in a:
        a.remove(d)
        a.add(i)
    else:
        a.add(d)
a=list(a)
a.sort()
print(len(a),*a)
