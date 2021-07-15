import collections as c
a=c.Counter(input() for _ in range(int(input())));b=a.most_common(1)[0][1]
print(*sorted([i for i,j in a.items() if j==b]),sep='\n')
