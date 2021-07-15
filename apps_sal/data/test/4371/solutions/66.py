S = input()

result = 10 ** 9
for i in range(len(S) - 3 + 1):
  result = min(result, abs(753 - int(S[i:i+3])))
  
print(result)
