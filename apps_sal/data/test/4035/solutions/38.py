A, B = [int(s) for s in input().split(' ')]
for p in range(10000):
    if int(p * 0.08) == A and int(p * 0.10) == B: 
        print(p)
        return
print((-1))

