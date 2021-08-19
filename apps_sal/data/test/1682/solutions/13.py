import sys


def make_gen(str):
    arr = str.split(' ')
    for item in arr:
        yield int(item)


s = input()
s = make_gen(s)
n = next(s)
k = next(s)
disc_price = [0] * n
norm_price = [0] * n
s = input()
s = make_gen(s)
for i in range(0, n):
    disc_price[i] = next(s)
s = input()
s = make_gen(s)
for i in range(0, n):
    norm_price[i] = next(s)
total = sum(norm_price)
new_price = []
for i in range(0, n):
    new_price.append(norm_price[i] - disc_price[i])
new_price.sort(reverse=True)
win_sum = 0
for i in range(0, k):
    win_sum += new_price[i]
while k < n and new_price[k] > 0:
    win_sum += new_price[k]
    k += 1
print(total - win_sum)
