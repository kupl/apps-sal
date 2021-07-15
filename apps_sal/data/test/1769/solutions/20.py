n = int(input())
m = int(input())
s = [str(i) for i in range(n+m+2-(n+1),n+m+2)]
s1 = [str(i) for i in range(n+m+2-(n+1)-1,0,-1)]
s.extend(s1)
print(' '.join(s))
