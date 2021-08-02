n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ca = [0, 0, 0, 0, 0]
cb = [0, 0, 0, 0, 0]

for i in a:
    ca[i - 1] += 1

for i in b:
    cb[i - 1] += 1

c = 0
for i in range(5):
    if (ca[i] + cb[i]) % 2 == 0:
        c += (max(ca[i], cb[i]) - min(ca[i], cb[i])) // 2
    else:
        print(-1)
        return
print(c // 2)
