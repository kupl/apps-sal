n = int(input())
t = list(map(int, input().split()))
tcopy = t[::-1]
tbool = [False] * len(t)
ans = 0
for i in range(len(t)):
    if not tbool[len(t) - i - 1]:

        ans += 1
        j = len(t) - i - 1
        while not tbool[j]:
            tbool[j] = True
            j = t[j] - 1
            if j < 0:
                break

        tbool[len(t) - i - 1] = True
print(ans)
