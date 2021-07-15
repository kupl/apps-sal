def main():
  s = str(input())
  s_ = set(list(s))
  t =  str(input())
  t_ =  set(list(t))
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  if t_ <= s_:
    length_s = len(s)
    
    res = [[length_s]*(26)  for _ in range(length_s+1)]
    for i in range(length_s-1, -1, -1):
      for j in range(26):
        if s[i] == alphabet[j]:
          res[i][j] = i+1
        else:
          res[i][j] = res[i+1][j]
    ans = 0
    now = 0
    for i in range(len(t)):
      for j in range(26):
        if t[i] == alphabet[j]:
          ans += res[now][j]-now
          now = res[now][j]
          if now == length_s:
            if t[i] == s[-1]:
              now = 0
            else:
              ans += res[0][j]
              now = res[0][j]
    print(ans)
  else:
    print(-1)
if  __name__  == "__main__":
  main()
