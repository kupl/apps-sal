n, m = [int(_) for _ in input().split()]
trans = {}

def better(a,b):
    if len(a) <= len(b):
        return a
    else:
        return b
    
for i in range(m):
    a,b = input().split()
    trans[a] = better(a,b)
    trans[b] = better(a,b)
    
l = input().split()
s = ""
for i in l:
    s += trans[i] + " "
    
print(s)

