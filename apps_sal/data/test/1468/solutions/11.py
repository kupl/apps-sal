n = int(input())
inp = [0] * n
for i in range(n):
    inp[i] = input()


def common_str(a, b):
    l = 1
    for i in range(1, len(a)):
        if a[i] != b[i]:
            break
        l += 1
    return a[:l]


for i in range(n - 1, 0, -1):
    if inp[i] < inp[i - 1]:
        inp[i - 1] = common_str(inp[i], inp[i - 1])
print('\n'.join(inp))
