N = int(input())
h = list(map(int, input().split()))

l = 0
flag = 1
count = 0
while l < N:
    while h[l] == 0:
        l += 1
        if l == N:
            flag = 0
            break
    if flag == 1:
        if l == N - 1:
            r = N - 1
        else:
            r = l + 1
            while h[r] != 0:
                r += 1
                if r == N:
                    break
            r -= 1
        for k in range(l, r + 1):
            h[k] -= 1
        count += 1
        # print(h)
    elif flag == 0:
        break
print(count)
