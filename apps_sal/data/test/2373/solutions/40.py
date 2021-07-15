n = int(input())
lis = [0]+list(map(int, input().split())) +[0]

total = 0

for i in range(1, n+1):
    if i == lis[i]:
        t = lis[i]
        lis[i] = lis[i+1]
        lis[i+1] = t
        total += 1

print(total)
