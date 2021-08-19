def read_nums():
    return list(map(int, input().split()))


(w, l) = read_nums()
rocks = read_nums()
cur_sum = sum(rocks[0:l])
min_sum = cur_sum
for i in range(l, len(rocks)):
    cur_sum -= rocks[i - l]
    cur_sum += rocks[i]
    min_sum = min(min_sum, cur_sum)
print(min_sum)
