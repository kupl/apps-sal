N = int(input())
H = list(map(lambda x: -int(x), input().split())) + [0]
cnt = 0

for i in range(N):
    while H[i] < 0:
        H[i] += 1
        j = i + 1
        while H[j] < 0:
            H[j] += 1
            j += 1
        cnt += 1

print(cnt)
