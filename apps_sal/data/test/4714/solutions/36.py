a, b = map(int, input().split())

result = 0
for x in range(a, b+1):
  if str(x) == ''.join(reversed(str(x))):
    result += 1
print(result)
