def input2():
    return map(int, input().split())


def input_array():
    return list(map(int, input().split()))


(n, m, c) = input2()
B = input_array()
A = [input_array() for _ in range(n)]
count = 0
for a in A:
    tmp = c
    for i in range(m):
        tmp += a[i] * B[i]
    if tmp > 0:
        count += 1
print(count)
