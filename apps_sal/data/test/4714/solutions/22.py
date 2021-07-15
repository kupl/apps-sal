A,B = map(int,input().split())

cnt = 0
for i in range(A,B+1):
  s = str(i)
  half = len(s) // 2
  add = len(s) % 2
  #print(s,-1, s[0:half],-1, s[half+add:][::-1])
  if s[0:half] == s[half+add:][::-1]:
    cnt += 1
    
print(cnt)
