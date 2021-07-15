koman=int(input())
num = []
n = koman
while n != 0:
  num.append(n % 10)
  n//=10



if num[0]==7 or num[1]==7 or num[2]==7:
    print("Yes")
else :
    print("No")

