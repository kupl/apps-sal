N = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(N):
    while(True):
        if a[i] == 0:
            break
        if a[i] % 2 == 0:
            a[i] = a[i] // 2
            s = s + 1
        else:
            break
print(s)
