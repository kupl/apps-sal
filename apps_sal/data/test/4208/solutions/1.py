import string
def ind(x):
  sample=list(string.ascii_lowercase)
  if x=="?":
    return 26
  else:
    return sample.index(x)
def main():
  n=int(input())
  l=input()
  r=input()
  l_arr=[[] for x in range(27)]
  r_arr=[[] for x in range(27)]

  for x in range(n):
    l_arr[ind(l[x])].append(x+1)
    r_arr[ind(r[x])].append(x+1)
  count=0
  pair=[]
  for x in range(26):
    while len(l_arr[x])!=0 and len(r_arr[x])!=0:
      pair.append((l_arr[x][-1],r_arr[x][-1]))
      del l_arr[x][-1]
      del r_arr[x][-1]
      count+=1
  for x in range(26):
    while len(l_arr[-1])!=0 and len(r_arr[x])!=0:
      pair.append((l_arr[-1][-1],r_arr[x][-1]))
      del l_arr[-1][-1]
      del r_arr[x][-1]
      count+=1
  for x in range(26):
    while len(l_arr[x])!=0 and len(r_arr[-1])!=0:
      pair.append((l_arr[x][-1],r_arr[-1][-1]))
      del l_arr[x][-1]
      del r_arr[-1][-1]
      count+=1
  for x in range(26):
    while len(l_arr[-1])!=0 and len(r_arr[-1])!=0:
      pair.append((l_arr[-1][-1],r_arr[-1][-1]))
      del l_arr[-1][-1]
      del r_arr[-1][-1]
      count+=1
  print(count)
  for x in range(count):
    print(pair[x][0],end=" ")
    print(pair[x][1])
  
      
main()

