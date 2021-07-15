n=int(input())

for a in range(1,100):
    for b in range(1,100):
        if pow(3,a)+pow(5,b)==n:
            print("{} {}".format(a,b))
            return
print(-1)
