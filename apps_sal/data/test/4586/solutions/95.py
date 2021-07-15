N = input()

for i in range(2):
   if N[i:i+3] == 3 * N[i]:
      print('Yes')
      return

print('No')
