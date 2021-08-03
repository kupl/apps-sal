a = input()
b = input()
l = max(len(a), len(b))

for i, j in zip(a.zfill(l), b.zfill(l)):
    if int(i) > int(j):
        print("GREATER")
        break
    elif int(i) < int(j):
        print("LESS")
        break
else:
    print("EQUAL")
