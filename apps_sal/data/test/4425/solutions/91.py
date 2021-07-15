n, k = map(int, input().split())
prob = [0]*n
for i in range(1, n+1):
  j = 0
  while i*(2**j) < k:
    j += 1
  prob[i-1] = (1/n)*(1/2)**j

print(sum(prob))
