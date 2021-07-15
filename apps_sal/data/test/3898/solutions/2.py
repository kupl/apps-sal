readInts=lambda: list(map(int, input().split()))

n=int(input())
a=readInts()
a.remove(0)
b=readInts()
b.remove(0)
pos=a.index(b[0])
a=a[pos:]+a[:pos]
print('YES' if a==b else 'NO')
