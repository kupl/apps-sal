n = int(input())
l = list(map(int,input().split())) 
if 0 in l:
    print("0")
    return
result = l[0]
l.pop(0)
for data in l:
    result *= data
    if result > 10 ** 18:
        result = -1
        break
print(result)
