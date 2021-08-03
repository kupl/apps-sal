n = int(input())

sequence = [float('-inf')] + [int(i) for i in input().split()] + [float('inf')]

f1 = [0] * n
f2 = [0] * n
f3 = [True if sequence[i + 1] - sequence[i - 1] >
      1 else False for i in range(1, len(sequence) - 1)]
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

f = [f1[i] + f2[i] + 1 if f3[i]
     else max(f1[i], f2[i]) + 1 for i in range(0, n)]

max_len = max(f)

print(max_len)

'''
n = int(input())

sequence = [float('-inf')] + [int(i) for i in input().split()] + [float('inf')]

len_1 = 1
len_2 = 0
max_len = 1

i = 1
while(i < n):
    if sequence[i] < sequence[i + 1]:
        len_1 += 1
        i += 1
    else:
        l = len_1 + len_2 + 1
        if l > max_len:
            max_len = l
        len_1, len_2 = 1, len_1

        if sequence[i + 2] - sequence[i] <= 1:
            if sequence[i + 1] - sequence[i - 1] > 1:
                len_2 -= 1
            else:
                len_2 = 0
            i += 1
        else:
            i += 2

if max_len < len_1 + len_2 + 1:
    max_len = len_1 + len_2 + 1

if max_len > n:
    max_len = n

print(max_len)
'''
