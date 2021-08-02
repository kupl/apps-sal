v = int(input())
a = [-1] + list(map(int, input().split()))
q = [0] * 10
if v < min(a[1:]):
    print(-1)
else:
    top_digit = -1
    for i in range(1, 10):
        if a[i] == min(a[1:]):
            top_digit = i
    q[top_digit] = v // a[top_digit]
    rem = v % a[top_digit]
    for i in range(9, top_digit, -1):
        if a[i] - a[top_digit] <= rem:
            add = min(rem // (a[i] - a[top_digit]), q[top_digit])
            q[i] += add
            q[top_digit] -= add
            rem = rem - add * (a[i] - a[top_digit])
    print("".join([str(i) * q[i] for i in range(9, 0, -1)]))
