N = int(input())
flg = False
for i in range(1,10):
    if N%i==0 and N//i<10:
        flg=True
        break
if flg:
    print("Yes")
else:
    print("No")
