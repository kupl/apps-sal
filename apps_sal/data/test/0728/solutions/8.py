from sys import stdin, stdout
input = stdin.readline
n = int(input())
a = list(map(int, input().split()))
l = a[0]
ans = 0
ops = a[1:]
ops = sorted(ops, reverse=True)
max_op = ops[0]
while l <= max_op:
    for (i, el) in enumerate(ops):
        if el == max_op:
            ops[i] -= 1
            ans += 1
            l += 1
            if l > max_op:
                break
    max_op = max(ops)
stdout.write(str(ans))
