n = int(input())

a = list(map(int, input().split()))

diffs = [a[0]]

for i in range(1,n):
    diffs.append(a[i] - a[i-1])

output = []
for l in range(1,n+1):
    flag = True

    for i in range(l, n):
        if diffs[i] != diffs[i-l]:
            flag = False
            break

    if flag:
        output.append(l)

print(len(output))

for i in output:
    print(i, end=" ")

