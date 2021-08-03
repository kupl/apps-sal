n = int(input())
someStr = 'aabb'
resultStr = someStr * (n // 4) + someStr[0:n % 4:]
print(resultStr)
