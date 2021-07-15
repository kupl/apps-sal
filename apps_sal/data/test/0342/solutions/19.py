a, b, c = map(int, input().split())
q = c * 2 + min(a, b) * 2
if a!=b:
    q+=1
print(q)
