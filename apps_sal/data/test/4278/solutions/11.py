n = int(input())
L = ["".join(sorted(input())) for i in range(n)]


from collections import Counter
L = Counter(L)

def num(n):
    return n*(n-1)//2
    
cnt = 0  
for v in L.values():
    cnt +=num(v)
print(cnt)
