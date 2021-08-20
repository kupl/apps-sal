N = int(input())
a = list(map(int, input().split()))
cnt1 = 0
li1 = []
for i in range(1, N):
    M = max(a)
    num = 0
    for j in range(N):
        if a[j] == M:
            n = j
    if a[i] < a[i - 1]:
        if M <= 0:
            cnt1 = -1
            break
        num += -((-a[i - 1] + a[i]) // M)
        if num < 0 or num > 2 * N:
            cnt1 = -1
            break
        a[i] += num * M
        for j in range(num):
            li1.append([n + 1, i + 1])
        cnt1 += num
cnt2 = 0
li2 = []
for i in range(1, N):
    M = min(a)
    num = 0
    for j in range(N):
        if a[j] == M:
            n = j
    if a[N - i] < a[N - i - 1]:
        if M >= 0:
            cnt2 = -1
            break
        num += -((-a[N - i - 1] + a[N - i]) // -M)
        if num < 0 or num > 2 * N:
            cnt2 = -1
            break
        a[N - i - 1] += num * M
        for j in range(num):
            li2.append([n + 1, N - i])
        cnt2 += num
if cnt1 <= 2 * N and cnt1 >= 0:
    print(cnt1)
    for x in li1:
        print(*x)
else:
    print(cnt2)
    for x in li2:
        print(*x)
