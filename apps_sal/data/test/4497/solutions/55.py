N = int(input())
counter = 0
while N >= 2:
  N //= 2
  counter +=1
ans = 2**counter
print(ans)
