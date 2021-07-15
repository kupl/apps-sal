def get_unique_list(seq):
  seen = []
  return [x for x in seq if x not in seen and not seen.append(x)]

n=int(input())
a=[]
for i in range(n):
  a.append(int(input()))

b=get_unique_list(a)
print(len(b))
