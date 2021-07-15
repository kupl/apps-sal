a,b = map(int,input().split())
s = list(map(int,input().split()))
num1 =0
num2 =0
if b ==0:
  print(a)
  return
for i in range(100):
    num1 = a-i
    num2 = a+i
    if not num1 in s and not num2 in s:
        print(num1)
        return
    if not num1 in s:
        print(num1)
        return
    if not num2 in s:
        print(num2)
        return
