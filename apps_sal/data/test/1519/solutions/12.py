n, l, a = list(map(int, input().split()))

arr = []
for k in range(n):
        s, e = input().split()
        s, e = int(s), int(e)
        arr.append((s, e))

arr.append((0, 0))
arr.append((l, 0))

arr.sort()

c = 0

for i in range(len(arr)-1):
        c += (arr[i+1][0] - arr[i][0] - arr[i][1]) // a;

print(c)

