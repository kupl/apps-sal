n = int(input())
h = [int(x) for x in input().split()]

cnt = 1

for i in range(1, n):
    for j in range(i):
        if(h[i] < h[j]):
            break
        if(j == (i - 1)):
            cnt += 1

print(cnt)
