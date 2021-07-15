def main():
  S = input()
  j = 0
  m = S[0]
  ls = []
  for i in range(len(S)):
    if m!=S[i]:
      ls.append(i-j)
      j = i
      m = S[i]
  ls.append(len(S)-j)
  N = len(ls)
  if N<3:
    print(max(ls))
  else:
    ans = float('inf')
    sls = [ls[0]]
    for i in range(1,N):
      sls += [sls[-1]+ls[i]]
    ans = min(max(sls[i], sls[-1]-sls[i]) for i in range(N-1))
    print(ans)

def __starting_point():
  main()
__starting_point()
