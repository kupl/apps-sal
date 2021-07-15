n = int(input())
ans = False
for i in range(1,10):
    if n%i==0 and n//i<10 and n<=81:
        ans=True
        break
print("Yes" if ans==True else "No")
