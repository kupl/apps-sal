# B - Many 110
N = int(input())
T = input()
ans = 10 ** 10

if T == '1':
  print((ans * 2))
elif T == '0' or T == '11' or T == '110':
  print(ans)
else:
  if T.startswith('10'):
    T = T[2:]
    ans -= 1
  elif T.startswith('0'):
    T = T[1:]
    ans -= 1
    
  if T.endswith('11'):
    T = T[:len(T)-2]
    ans -= 1
  elif T.endswith('1'):
    T = T[:len(T)-1]
    ans -= 1

  if len(T) % 3 == 0:
    for i in range(0, len(T), 3):
      if T[i:i+3] == '110':
        ans -= 1
      else:
        print((0))
        return
    
    print((ans+1))
  else:
    print((0))

