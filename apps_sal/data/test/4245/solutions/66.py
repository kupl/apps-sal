A, B = list(map(int, input().split()))

N = 0
sum = 1

while (sum < B):
     N += 1
     sum = A + (A-1)*(N-1)

     if sum >= B:
         break

ans = N

print(ans)

