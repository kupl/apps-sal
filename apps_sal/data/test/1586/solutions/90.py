N = int(input())
if N%2 == 1 :
    print(0)
    return
n = 0
i = 0
for i in range(1,26) :
    n += N//((5**i)*2)

print(n)
