n = int(input())
sequence = [float('-inf')] + [int(i) for i in input().split()] + [float('inf')]
f1 = [0] * n
f2 = [0] * n
f3 = [True if sequence[i + 1] - sequence[i - 1] > 1 else False for i in range(1, len(sequence) - 1)]
len_1 = 0
len_2 = 0
l = len(sequence) - 1
for i in range(1, len(sequence) - 1):
    f1[i - 1] = len_1
    f2[i - 1] = len_2
    if sequence[i] > sequence[i - 1]:
        len_1 += 1
    else:
        len_1 = 1
    if sequence[l - i] < sequence[l - i + 1]:
        len_2 += 1
    else:
        len_2 = 1
f2 = f2[::-1]
f = [f1[i] + f2[i] + 1 if f3[i] else max(f1[i], f2[i]) + 1 for i in range(0, n)]
max_len = max(f)
print(max_len)
"\nn = int(input())\n\nsequence = [float('-inf')] + [int(i) for i in input().split()] + [float('inf')]\n\nlen_1 = 1\nlen_2 = 0\nmax_len = 1\n\ni = 1\nwhile(i < n):\n    if sequence[i] < sequence[i + 1]:\n        len_1 += 1\n        i += 1\n    else:\n        l = len_1 + len_2 + 1\n        if l > max_len:\n            max_len = l\n        len_1, len_2 = 1, len_1\n\n        if sequence[i + 2] - sequence[i] <= 1:\n            if sequence[i + 1] - sequence[i - 1] > 1:\n                len_2 -= 1\n            else:\n                len_2 = 0\n            i += 1\n        else:\n            i += 2\n\nif max_len < len_1 + len_2 + 1:\n    max_len = len_1 + len_2 + 1\n\nif max_len > n:\n    max_len = n\n\nprint(max_len)\n"
