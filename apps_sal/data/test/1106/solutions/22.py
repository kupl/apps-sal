n = 2**(int(input())+1)-1;
a = [0,0] + list(map(int,input().split()))
r = 0
while n>1:
  a[n//2] += max(a[n], a[n-1])
  r += abs(a[n]-a[n-1])
  n -= 2
print(r)

