a, b = input().split()

count = 0
for i in range(int(a), int(b) + 1):
    mylist = list(str(i))
    if mylist[0] == mylist[4] and mylist[1] == mylist[3]:
        count += 1

print(count)
