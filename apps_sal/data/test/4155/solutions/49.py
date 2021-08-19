N = int(input())
h = list(map(int, input().split()))
l = 0
flag = 1
count = 0
while l < N - 1:
    if h[l] == 0:
        l += 1
    elif h[l] != 0:
        r = l + 1
        while h[r] != 0:
            r += 1
            if r == N:
                break
        for k in range(l, r):
            h[k] -= 1
        count += 1
print(count + h[N - 1])
