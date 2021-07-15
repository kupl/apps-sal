n=int(input())
bits = list(map(int,input().split()))
ans = set()
for i in reversed(range(n)):
  for j in range(i+(i+1),n,i+1):
    bits[i] ^= bits[j]
  if bits[i] == 1:
    ans.add(i+1)
print(len(ans))
print(*ans)
