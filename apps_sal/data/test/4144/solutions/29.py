# 0を含まない: 9 ** n
# 9を含まない: 9 ** n
# 0と9を含まない: 8 ** n
# 0または9を含まない: 2 * 9 ** n - 8 ** n
# 0と9を含む: 10 ** 9 - 2 * 9 ** n + 8 ** n
def pow(a, x):
  if x == 0:
    return 1
  else:
    y, r = divmod(x, 2)
    sq = pow(a, y)
    if r == 1:
      return (sq * sq * a) % (10 ** 9 + 7)
    else:
      return (sq * sq) % (10 ** 9 + 7)
    
def __starting_point():
  n = int(input())
  print((pow(10, n) - 2 * pow(9, n) + pow(8, n)) % (10 ** 9 + 7))
__starting_point()
