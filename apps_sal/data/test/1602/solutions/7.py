n = int(input())
l = list(map(int, input().split()))
cnt = [0] * 30
for i in range(n):
    for j in range(30):
        if l[i] & 1 << j:
            cnt[j] += 1
options = [i for i in range(n)]
for i in range(29, -1, -1):
    newoptions = []
    if cnt[i] == 1:
        for idx in options:
            if l[idx] & 1 << i:
                newoptions.append(idx)
    if len(newoptions) > 0:
        options = newoptions
print(l[options[0]], end=' ')
for i in range(n):
    if i != options[0]:
        print(l[i], end=' ')
