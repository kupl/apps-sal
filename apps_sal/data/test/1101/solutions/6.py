n, k = [int(_) for _ in input().split()]
a = input()


def next_free(x):
    x += 1
    while x < n and a[x] == '1':
        x += 1
    return x


l = next_free(-1)
r = -1


k += 1
for _ in range(k):
    r = next_free(r)
i = l
dis = max(i-l, r-i)
next_i = next_free(i)
while True:
    cur_dis = max(i-l, r-i)
    next_dis = max(next_i - l, r - next_i)

    if cur_dis <= next_dis:
        break
    i = next_i
    dis = min(dis, next_dis)
    next_i = next_free(i)


while True:
    r = next_free(r)
    if r >= n:
        break
    l = next_free(l)
    if i < l:
        i = l
    prev_dis = max(i-l, r-i)
    dis = min(dis, prev_dis)
    m = next_free(i)
    while m <= r:
        cur_dis = max(m-l, r-m)
        if cur_dis >= prev_dis:
            break
        prev_dis = cur_dis
        i = m
        dis = min(dis, cur_dis)
        m = next_free(m)

print(dis)


# binary search the ANSWER!!
# choose an answer and check if it works
# array [i] keeps track of how many zeros are before it

