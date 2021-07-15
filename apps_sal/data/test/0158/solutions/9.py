import sys, os

n = int(input())
n *= 2
data = list(map(int, input().split()))
data = sorted(data)
data1 = data[:n//2]
data2 = data[n//2:]
for i in range(n // 2):
    if data1[i] in data2:
        print("NO")
        return
        sys.exit
        os.abort()
print("YES")

