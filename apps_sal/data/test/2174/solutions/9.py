n = int(input())
p = list(map(int,input().split()))
total = 0
j = 1
for i in sorted(p):
    total += abs(i-j)
    j+=1
print(total)
