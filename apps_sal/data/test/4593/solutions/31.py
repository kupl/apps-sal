x = int(input())
pr = [1]
for i in range(2, 32):
    for j in range(2, 10):
        if (i ** j <= 1000) & (i ** j not in pr):
            pr.append(i ** j)
print(max([k for k in pr if k <= x]))
