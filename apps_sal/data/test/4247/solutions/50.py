n = int(input())
p = [int(s) for s in input().split()]
count = 0
for i in range(len(p)-2):
    if p[i] < p[i+1] < p[i+2] or p[i] > p[i+1] > p[i+2] :
        count += 1
print(count)
