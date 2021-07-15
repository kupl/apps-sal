N = int(input())
A = [int(input()) for i in range(N)]

sorted_a = sorted(A, reverse= True)
max_val, next_max_val = sorted_a[:2]
for a in A:
  if a == max_val:
    print(next_max_val)
  else:
    print(max_val)
