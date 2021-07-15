N = int(input())
D,X = input().split()
x = 0
for n in range(N):
  An = int(input())
  x += 1+(int(D)-1)//An
c = x+int(X)
print(c)

