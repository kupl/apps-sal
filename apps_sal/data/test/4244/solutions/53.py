n = int(input())
x = [int(s) for s in input().split()]
hp = []
for i in range(min(x),max(x) + 1):
    sum_ = 0
    for j in x:
        sum_ = sum_ + (j - i)**2
    hp.append(sum_)
print(min(hp))
