N = int(input())
K = int(input())

out = 1
flg = 0
for i in range(N):
    if not flg:
        out *= 2
        if out > K:
            flg = 1
    else:
        out += K

print(out)
