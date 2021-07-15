N = int(input())
lst = input().split()

for i in range(N):
   lst[i] = int(lst[i])
lst.sort(reverse=True)

Alice = 0
Bob = 0

for i in range(N // 2):
   Alice += lst[2 * i]
   Bob += lst[(2 * i) + 1]

if N % 2 == 1:
   Alice += lst[-1]

print(Alice - Bob)
