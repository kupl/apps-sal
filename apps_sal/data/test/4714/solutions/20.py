ab = list(map(int, input().split()))
(a, b) = (ab[0], ab[1])
count = 0
for num in range(a, b + 1):
    str_num = str(num)
    str_num_reversed = ''.join(list(reversed(str_num)))
    if str_num == str_num_reversed:
        count += 1
print(count)
