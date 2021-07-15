n = int(input())
h = list(map(int, input().split()))

cnt = 0
for i in range(n):
    while h[i] > 0:
        h[i] -= 1 
        cnt += 1
        j = 1
        while i + j < n:
            if h[i + j] >= 1:
                h[i + j] -= 1
                j += 1
            else:
                break
print(cnt)
