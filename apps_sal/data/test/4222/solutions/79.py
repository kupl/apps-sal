n, k = list(map(int, input().split()))

sunuke = [False] * n

for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))

    for j in range(d):
        sunuke[a[j] - 1] = True

cnt = 0
for i in range(n):
    if sunuke[i] == False:
        cnt += 1

print(cnt)
