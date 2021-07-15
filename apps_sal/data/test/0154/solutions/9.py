n = int(input())
exist = list()
exist.append(1)
exist.append(2)
exist.append(4)
exist.append(5)
prev1 = 4
prev2 = 5
while prev2 < n:
    t1 = 1 + 2*(max(prev1, prev2) - (min(prev1, prev2) + 1) % 2)
    t2 = 1 + (max(prev1, prev2) - (min(prev1, prev2) + 1) % 2) + (max(prev1, prev2) - (min(prev1, prev2)) % 2)
    prev1 = t1
    prev2 = t2
    exist.append(prev1)
    exist.append(prev2)
if n in exist:
    print(1)
else:
    print(0)
