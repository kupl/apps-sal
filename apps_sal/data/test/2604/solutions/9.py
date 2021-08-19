3


def read_ints():
    return [int(i) for i in input().split()]


(r, d) = read_ints()
n = int(input())
cnt = 0
for i in range(n):
    (x, y, r_i) = read_ints()
    if x ** 2 + y ** 2 >= (r - d + r_i) ** 2 and x ** 2 + y ** 2 <= (r - r_i) ** 2:
        cnt += 1
print(cnt)
