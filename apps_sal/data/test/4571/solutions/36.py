n, m = map(int, input().split())
value = 1900*m+(n-m)*100
p = 2**m
ans = value*p
print(ans) 
