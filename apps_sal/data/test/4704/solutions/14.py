n = int(input())
a = list(map(int, input().split()))
sa = sum(a) # sum a
cs = 0 # cards sunuke
arr = []

for i in range(n-1):
  cs += a[i]
  ca = sa -cs #cards araiguma
  arr.append(abs(cs-ca))
 
print(min(arr))
