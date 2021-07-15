N, X = map(int, input().split())
l = [1]
for i in range(N):
  l.append(2*l[-1]+1)

def main(n, x, ans):
  nonlocal X
  nonlocal l
  if n == 0:
    return ans+1
  elif x==1:
    return ans
  elif x==2*l[n]-1:
    return ans+2*l[n-1]+1
  elif x == l[n]:
    return main(n-1, x-2, ans+1)
  elif x < l[n]:
    return main(n-1, x-1, ans)
  else:
    return main(n-1, x-2*l[n-1]-1, ans+l[n-1]+1)
  
a = main(N, X, 0)
print(a)
