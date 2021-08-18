n = int(input())
lis = list(map(int, input().split()))
total = []
count = 0
for i in range(n):

    if lis[i] != 0:
        count += 1
        total.append(count)
    elif lis[i] == 0:
        count = 0

print(max(total)) if len(total) > 0 else print(0)
