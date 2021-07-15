n, n1, n2 = map(int, input().split())
data = list(sorted(map(int, input().split()), reverse = True))
if (n1 > n2):
  n1, n2 = n2, n1
print(sum(data[0:n1])/n1 + sum(data[n1:n1+n2])/n2)
