a,b,c,d = map(int,input().split())

s1 = set(range(a,b+1))
s2 = set(range(c,d+1))


print(max(len(s1 & s2)-1,0))
