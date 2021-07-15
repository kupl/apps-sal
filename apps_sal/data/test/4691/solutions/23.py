N = int(input())
C0 =[]
C1 =[]
C2 =[]
C3 =[]
for i in range(N):
  S = input()
  if S == 'AC':
    C0.append(S)
  elif S == 'WA':
    C1.append(S)
  elif S == 'TLE':
    C2.append(S)
  elif S == 'RE':
    C3.append(S)

print('AC x ', len(C0))
print('WA x ', len(C1))
print('TLE x ', len(C2))
print('RE x ', len(C3))
