a = input()
b = input()
k = min(len(a), len(b))
i = 0
while i < k:
    if a[len(a)-1-i] == b[len(b)-1-i]:
        i+=1
    else:
        break
print(len(a)+len(b)-2*i)

