n = int(input())
s = list(map(int,input().split()))
a,b=  [int(x)-1 for x in input().split()]
if a > b: a,b=b,a
tot = sum(s[a:b])
print(min(tot, sum(s)-tot))

