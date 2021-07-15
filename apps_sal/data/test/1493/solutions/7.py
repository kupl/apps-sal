n,m = list(map(int,input().split()))
for i in range(0,n):
       s = input()
       ans = ""
       for j in range(0,m):
              if s[j] == '.':
                     if (i+j)&1==1:
                            ans += "W"
                     else:
                            ans += "B"
              else:
                     ans += s[j]
       print(ans)
                     
                        

