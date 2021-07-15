def PanlidromicCharacteristics(string):
  n = len(string)
  res = [[0 for i in range (n)] for j in range (n)]
  count = [0 for i in range (n + 1)]
  # for i in range (n):
  #   res[i][i] = 1
  #   count[1] += 1
  
  for length in range (1, n + 1):
    for i in range (n-length + 1):
      j = i + length - 1
      if length == 1:
          res[i][j] = 1
      elif length == 2 and string[i] == string[j]:
          res[i][j] = 2
      elif string[i] == string[j] and res[i + 1][j - 1] > 0:
        res[i][j] = res[i][i + length//2 - 1]  + 1        
      count[res[i][j]] += 1
      
  # k-palindrome is also a (k - 1)-palindrome
  for i in range (len(count) - 1, 0, -1):
    count[i - 1] += count[i]
  for i in range (1, len(count)):
    print(count[i], end = " ")
  return 
  
string = input()
PanlidromicCharacteristics(string)
