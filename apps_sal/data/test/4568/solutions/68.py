n=int(input())
s=input()

result = 0
for i in range(1,n):
  x = s[:i]
  y = s[i:]
  x_set = set(x)
  y_set = set(y)
  num = x_set & y_set
  result = max(result, len(num))
print(result)

