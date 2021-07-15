s,p=[int(x) for x in input().split()]
i = 1
while i*i <= p:
    if p % i == 0:
        if i+p//i==s:
            print("Yes")
            return
    i += 1
print("No")
