n = int(input())
m = list(map(int, input().split()))
r = list(map(int, input().split()))
count = 0.0
for i in range(100000):
    for j in range(len(m)):
        if i % m[j] == r[j]:
            count += 1
            break
print(count / 100000.0)
