#B問題

#x匹　y本

x, y = map(int, input().split())
counter = 0
# iは鶴　jは亀
for i in range(0,x+1):
    j = x - i
    if (2*i + 4*j == y):
        counter += 1
        break
if counter >= 1:
    print("Yes")
else:
    print("No")
