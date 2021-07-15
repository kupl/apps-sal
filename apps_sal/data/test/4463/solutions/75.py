def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  S=input()
  T=input()
  if S==T:
    print("No")
    return
  if S in T:
    print("Yes")
    return
  s=list(S)
  t=list(T)
  
  s.sort()
  t.sort(reverse=True)
  if s==t:
    print("No")
    return
  
#  if(len(s)<len(t)):
#    print("Yes")
#    return
  for i in range(min(len(s),len(t))):
    if ord(s[i])>ord(t[i]):
      print("No")
      return
    elif ord(s[i])<ord(t[i]):
      print("Yes")
      return
  print("No")
  return
main()
