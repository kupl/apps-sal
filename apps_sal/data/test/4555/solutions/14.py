a,b,k=map(int,input().split())

if k>=b-a+1:
  for i in range(a,b+1):
    print(i)

else:
  a_set={i for i in range(a,a+k)}
  b_set={i for i in range(b-k+1,b+1)}

  ans_set = sorted(a_set | b_set)

  for i in ans_set:
    print(i)
