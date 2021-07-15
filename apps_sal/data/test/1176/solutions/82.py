
n = int(input())
aa = list(map(int, input().split()))
bb = [abs(a) for a in aa]

if sum(x<0 for x in aa) % 2 == 0:
  print(sum(bb))
else:
  
  print(sum(bb)-2*min(bb))
