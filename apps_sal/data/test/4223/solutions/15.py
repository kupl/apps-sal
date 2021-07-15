n=int(input())
s=input()
num=n
for i in range(1,n):
    if s[i-1]==s[i]:
        num-=1
print(num)

