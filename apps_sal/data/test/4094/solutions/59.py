k = int(input())
a = 7
if k == 1 or k == 7 :
    print((1))
    return

for i in range(k):
    a *= 10
    a += 7
    a %= k
    if a == 0 :
        print((i+2))
        return
print((-1))

