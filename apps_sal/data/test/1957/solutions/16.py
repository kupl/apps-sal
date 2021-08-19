(n, a, b) = [int(i) for i in input().split(' ')]
sizes = [int(i) for i in input().split(' ')]
st = sum(sizes)
s = sizes[0] * a / b
sb = st - s
blockable = sorted(sizes[1:], reverse=True)
blocked_no = 0
blocked_amount = 0
for i in range(len(blockable)):
    if blocked_amount < sb:
        blocked_no += 1
        blocked_amount += blockable[i]
    else:
        break
print(blocked_no)
