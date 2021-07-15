
t = int(input())
for _ in range(t):
  n = int(input())
  s = input()
  ans = [(s,1),(s[::-1],n)]
  for i in range(2,n):
    if (n-i+1)%2:
      x = "".join((s[i-1:],s[i-2::-1]))
      ans.append((x,i))
    else:
      x = "".join((s[i-1:],s[:i-1]))
      ans.append((x,i))
  ans.sort()
  print(*ans[0],sep="\n")
