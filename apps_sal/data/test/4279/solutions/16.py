n = int(input())
k_list = []
for i in range(n):
    k_list.append(int(input()))

digits = [0]
w = 1
milestone = 10
str_seq = ''
for i in range(1, 100000):
    if i == milestone:
        w += 1
        milestone *= 10
    digits.append(digits[i - 1] + w)
    str_seq += str(i)
digits_in_sequence = [0]

for i in range(1, 100000):
    digits_in_sequence.append(digits_in_sequence[i - 1] + digits[i])

k_list = list(enumerate(k_list))
k_list.sort(key=lambda x: x[1])

res = [''] * n
k_i = 0
d_i = 0
while k_i != len(k_list):
    d = digits_in_sequence[d_i]
    ind, k = k_list[k_i]
    if d >= k:
        from_one = (k - digits_in_sequence[d_i - 1])
        res[ind] = str_seq[from_one - 1]
        k_i += 1
    else:
        d_i += 1
print('\n'.join(res))

