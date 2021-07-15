N = int(input())
hen = []

hen = list(int(x) for x in input().split())
hen.sort()
#print(hen)
#hen_u = set(hen)
#print(hen_u)
tri = 0

for a in hen:
    for b in hen:
        if(a == b)or (a > b):
            continue
        for c in hen:
            if(a == c)or(b == c) or (a > c) or (b > c):
                continue
            if(a+b >c)and(b+c >a)and(c+a >b):
                tri += 1

print(tri)
