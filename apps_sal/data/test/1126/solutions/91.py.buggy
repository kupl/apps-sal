N, X, M = list(map(int, input().split()))

A = X
loop_dict = {A: 1}
ct = 1
while True:
    ct += 1
    A = A ** 2 % M
    if A in loop_dict:
        break
    else:
        loop_dict[A] = ct
        if ct == N:
            # 一周しなかった場合
            print((sum(loop_dict)))
            return

loop_length = len(loop_dict) - loop_dict[A] + 1
tail_length = loop_dict[A] - 1
loop = [0] * loop_length
tail = [0] * tail_length

for x, i in list(loop_dict.items()):
    if i <= tail_length:
        tail[i - 1] = x
    else:
        loop[i - tail_length - 1] = x

d, m = divmod(N - tail_length, loop_length)
print((sum(tail) + sum(loop) * d + sum(loop[:m])))
