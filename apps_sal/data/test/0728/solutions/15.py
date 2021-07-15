n = int(input())
a = list(map(int, input().split(" ")))
l = a[0]
c = a[1:]
result = 0
while(True):
    c.sort(reverse=True)
    if l > c[0]:
        break
    else:
        l += 1
        c[0] -= 1
        result+=1

print(result)
    

