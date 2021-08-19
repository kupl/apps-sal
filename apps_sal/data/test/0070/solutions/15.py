# your code goes here
n, k = input().strip().split()
k = int(k)
n_ = ""
count = 0
count_rem = 0
possible = False
for i in reversed(n):
    # print(count, count_rem)
    if count >= k:
        possible = True
        break
    elif i is "0":
        count += 1
    else:
        count_rem += 1

if possible:
    print(count_rem)
elif count is 0:
    print(len(n))
else:
    print(len(n) - 1)
