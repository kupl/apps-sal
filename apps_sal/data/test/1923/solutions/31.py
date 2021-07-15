n = int(input())
l = list(map(int,input().split()))
answer = 0
l = sorted(l)
for i in range(0,2*n,2):
  answer +=l[i]
print(answer)
