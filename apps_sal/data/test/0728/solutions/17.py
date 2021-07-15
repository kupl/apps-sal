n = int(input())
a = list(map(int, input().split()))

cnt = 0
while max(a[1:]) >= a[0]:
    i = 0
    for j in range(len(a)):
        if a[j] == max(a):
            i = j
    a[i] -= 1
    a[0] += 1
    cnt += 1
print(cnt)

