n = int(input())
a = list(map(int, input().split()))
data = [0] * (10**5 + 2)
for i in a:
    data[i] += 1
    data[i + 1] += 1
    data[i + 2] += 1
print(max(data))
