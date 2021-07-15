a,b,c = list(map(int,input().split()))
d,e,f = list(map(int,input().split()))
g,h,i = list(map(int,input().split()))

x = []
y = [a,b,c,d,e,f,g,h,i]

n = int(input())
for s in range(n):
  x.append(int(input()))

for m in range(9):
  if y[m] in x:
      y[m] = 0

if y[0] == y[1] == y[2] == 0:
    print("Yes")
elif y[3] == y[4] == y[5] == 0:
    print("Yes")

elif y[6] == y[7] == y[8] == 0:
    print("Yes")

elif y[0] == y[3] == y[6] == 0:
    print("Yes")

elif y[1] == y[4] == y[7] == 0:
    print("Yes")

elif y[2] == y[5] == y[8] == 0:
    print("Yes")

elif y[0] == y[4] == y[8] == 0:
    print("Yes")

elif y[2] == y[4] == y[6] == 0:
    print("Yes")

else:

    print("No")

