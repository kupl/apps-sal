s = input()
k = int(input())
seen = set()
i = 1
 
while i<=k:
  for j in range(len(s)):
    seen.add(s[j:j+i])
  i += 1
 
print(sorted(seen)[k-1])
