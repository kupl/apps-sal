n = int(input())
a = [int(x) for x in input().split()]

sum=0
a = sorted(a)
for c in a: sum+=c
avg = sum/n
count = 0
for c in a:
    if avg >= 4.5:
        break
    sum += 5-c
    avg = sum / n
    count += 1
print(count)

