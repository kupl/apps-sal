(n, t) = map(int, input().split())
tn = [int(num) for num in input().split()]
sum = 0
for i in range(len(tn)):
    if i < len(tn) - 1:
        if tn[i] + t < tn[i + 1]:
            sum += t
        else:
            sum += tn[i + 1] - tn[i]
    else:
        sum += t
print(sum)
