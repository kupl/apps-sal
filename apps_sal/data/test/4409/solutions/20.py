import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
output = []
maxi = 0
start = -1
counts = {}
for i in range(n):
    if a[i] not in counts.keys():
        counts[a[i]] = 0
    counts[a[i]] += 1
    if counts[a[i]] > maxi:
        start = i
        maxi = counts[a[i]]
for i in range(start, 0, -1):
    if a[i - 1] < a[i]:
        a[i - 1] = a[i]
        output.append('1 ' + str(i) + ' ' + str(i + 1))
    elif a[i - 1] > a[i]:
        a[i - 1] = a[i]
        output.append('2 ' + str(i) + ' ' + str(i + 1))
for i in range(start, n - 1):
    if a[i + 1] < a[i]:
        a[i + 1] = a[i]
        output.append('1 ' + str(i + 2) + ' ' + str(i + 1))
    elif a[i + 1] > a[i]:
        a[i + 1] = a[i]
        output.append('2 ' + str(i + 2) + ' ' + str(i + 1))
print(len(output))
for line in output:
    print(line)
