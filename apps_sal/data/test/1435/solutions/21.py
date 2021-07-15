
n = input()
i = 0
count = 1
a = 1
for i in range(1,len(n)):
    if int(n[i]) + int(n[i-1]) == 9:
        count+=1
    elif count%2!=0:
        a*=count//2 + 1
        count = 1
    else:
          count = 1
if count%2!=0:
    a*=count//2 + 1
print(a)

