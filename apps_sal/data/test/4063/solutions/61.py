n = int(input())
d = list(map(int,input().split()))
s = sorted(d)
t = n//2
print(s[t]- (s[t-1]+1)+1)
