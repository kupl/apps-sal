_, _ = list(map(int, input().strip().split()))

msg1 = list(map(int, input().strip().split()))
msg2 = list(map(int, input().strip().split()))

idx1, idx2 = 0, 0
count = 0

while idx1 < len(msg1):

    sum1, sum2 = msg1[idx1], msg2[idx2]

    while sum1 != sum2:

        if sum1 < sum2:
            idx1 += 1
            sum1 += msg1[idx1]

        else:
            idx2 += 1
            sum2 += msg2[idx2]

    idx1, idx2 = idx1 + 1, idx2 + 1

    count += 1

print(count)
