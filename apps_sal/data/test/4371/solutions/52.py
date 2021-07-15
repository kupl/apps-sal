A = list(input())
ans = list()
for i in range(len(A)-2):
  num = int(A[i])*100+int(A[i+1])*10+int(A[i+2])
  ans.append(abs(num-753))
print(min(ans))
