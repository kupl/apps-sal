n = int(input())

m = list()
for i in range(n):
    m.append(list(int(x) for x in input().split()))
m.sort();

k = 0
for i in range(n - 1):
    if m[i][1] > m[i + 1][1]:
        print("Happy Alex")
        k = 1
        break
    if k:
        break
if not k:
    print("Poor Alex")
