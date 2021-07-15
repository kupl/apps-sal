N = int(input())
S = input()
list = [0]*N
for i in range(N):
    A = S[:i]
    B = S[i:]
    A = set(A)
    B = set(B)
    for j in A:
      if j in B:
        list[i] += 1
list = sorted(list)
print(list[-1])
