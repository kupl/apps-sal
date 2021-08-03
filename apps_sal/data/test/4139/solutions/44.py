def f(v, K):
    nonlocal cnt
    v += str(K)
    if len(v) == len_ and int(v) <= N:
        if len(set(v)) == 3:
            cnt += 1
        return
    elif len(v) == len_:
        return
    f(v, 7)
    f(v, 5)
    f(v, 3)


N = int(input())
total = [0, 0]
for i in range(3, 10):
    temp = 3**i - (2**i * 3 - 3)
    total.append(temp)
len_ = len(str(N))
ans = sum(total[:len_ - 1])
cnt = 0
f('', '')
ans += cnt
print(ans)
