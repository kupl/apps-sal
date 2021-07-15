n = int(input())

ans = float("inf")
for i in range(1, int(n**0.5)+1):
  if n%i == 0:
    t = n//i
    if i-1+t-1 < ans: ans = i-1+t-1
print(ans)
