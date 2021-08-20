max_d = 18
max_index = [0] * max_d
num_dig_last = [0] * max_d
num_dig_all = [0] * max_d
num_dig_all_until = [0] * max_d
for i in range(max_d):
    max_index[i] = 10 ** i - 1
for i in range(1, max_d):
    n = 9 * 10 ** (i - 1)
    num_dig_last[i] = num_dig_last[i - 1] + n * i
    num_dig_all[i] = (num_dig_last[i - 1] + i + num_dig_last[i]) * n // 2
    num_dig_all_until[i] = num_dig_all_until[i - 1] + num_dig_all[i]
t = int(input())
for z in range(t):
    k = int(input())
    for i in range(max_d):
        if k <= num_dig_all_until[i]:
            x = num_dig_last[i - 1]
            p = k - num_dig_all_until[i - 1]
            l = 1
            r = 9 * 10 ** (i - 1)
            res = 0
            while l <= r:
                curr = (l + r) // 2
                if p <= curr * x + i * curr * (curr + 1) / 2:
                    res = curr
                    r = curr - 1
                else:
                    l = curr + 1
            prev = res - 1
            q = p - (prev * x + i * prev * (prev + 1) // 2)
            for j in range(max_d):
                if q <= num_dig_last[j]:
                    w = q - num_dig_last[j - 1]
                    r = w % j
                    x = w // j
                    if r != 0:
                        x += 1
                        r -= 1
                    else:
                        r = j - 1
                    number = 10 ** (j - 1) + x - 1
                    print(str(number)[r])
                    break
            break
