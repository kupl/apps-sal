
N = int(input())
l = list(map(int, input().split()))

flag_ary = [0] * (N + 1)

counter = 0
cur = 1
for i in l:
    if i == cur:
        counter += 1
        cur += 1
if counter == 0:
    print((-1))
else:
    print((N - counter))
