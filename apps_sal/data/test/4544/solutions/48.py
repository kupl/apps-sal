n = int(input())
lis = list(map(int, input().split()))
con = [0] * (10**5+2)

for v in lis:
  con[v] +=1
  con[v+1] += 1
  con[v+2] += 1

print(max(con))
