import math

n, n1, n2 = [int(x) for x in input().split()]
n1, n2 = min(n1, n2), max(n1, n2)
s = [int(x) for x in input().split()]
s.sort()
s.reverse()
s1 = s[:n1]
s2 = s[n1:n1 + n2]
print(sum(s1)/n1 + sum(s2)/n2)    

