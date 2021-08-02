N = input()
li = list(map(int, input().split()))
li.sort(reverse=True)
Alice = 0
Bob = 0
for i in range(len(li)):
    if (i + 1) % 2 == 1:
        Alice += li[i]
    if (i + 1) % 2 == 0:
        Bob += li[i]
print((Alice - Bob))
