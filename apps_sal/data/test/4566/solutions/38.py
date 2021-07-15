def actual(N, M, A, B):
    AB = A + B

    counts = [AB.count(i) for i in range(1, N + 1)]
    
    return '\n'.join(map(str, counts))

N, M = list(map(int, input().split()))
A, B = [], []
for _ in range(M):
  a, b = list(map(int, input().split()))
  A.append(a)
  B.append(b)
  
print((actual(N, M, A, B)))

