def solve(length, cities):
  result = 0
  lastP = None
  lastB = None
  lastR = None
  maxB = 0
  maxR = 0
  for idx, city in enumerate(cities):
    i, code = city
    if(code == 'B'):
      if(lastB != None):
        result += abs(i - lastB)
        maxB = max(maxB, abs(i - lastB))
      lastB = i
    if(code == 'R'):
      if(lastR != None):
        result += abs(i - lastR)
        maxR = max(maxR, abs(i - lastR))
      lastR = i
    if(code == 'P'):

      # B case
      if(lastB != None):
        result += abs(i - lastB)
        maxB = max(maxB, abs(i - lastB))

      # R case
      if(lastR != None):
        result += abs(i - lastR)
        maxR = max(maxR, abs(i - lastR))

      if(lastP != None):
        result += min(0, abs(i - lastP) - maxB - maxR)
      maxB = 0
      maxR = 0
      lastB = i
      lastR = i
      lastP = i
  return result      

def __starting_point():
  length = int(input())
  cities = []
  for i in range(length):
    data = input().split(" ")
    cities.append((int(data[0]), data[1]))
  result = solve(length, cities)
  print(result)

__starting_point()
