n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

m = [0] * 2
for i, j in l:
    m[(i + j) % 2] += 1
if m[0] * m[1] > 0:
    print(-1)
    return

if m[1] > 0:
    arm = [2**i for i in range(32)]
else:
    arm = [1] + [2**i for i in range(32)]

print(len(arm))
print(*arm)
for x, y in l:
    ans = []
    nx = x
    ny = y
    for i in arm[::-1]:
        if abs(nx) >= abs(ny):
            if nx >= 0:
                ans.append("R")
                nx -= i
            else:
                ans.append("L")
                nx += i
        else:
            if ny >= 0:
                ans.append("U")
                ny -= i
            else:
                ans.append("D")
                ny += i

    print(*ans[::-1], sep="")
