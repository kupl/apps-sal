n = int(input())
sh = list(map(int, input()))
mor = list(map(int, input()))
cnt = [0] * 10
for elem in mor:
    cnt[elem] += 1
cnt2 = cnt[:]
takes = 0
new_mor = [0] * n
for i in range(n):
    ptr = sh[i]
    while ptr < 10 and cnt[ptr] == 0:
        ptr += 1
    if ptr != 10:
        new_mor[i] = ptr
        cnt[ptr] -= 1
    else:
        ptr = 0
        while ptr < 10 and cnt[ptr] == 0:
            ptr += 1
        new_mor[i] = ptr
        cnt[ptr] -= 1
for i in range(n):
    if new_mor[i] < sh[i]:
        takes += 1
gives = 0
new_mor = [0] * n
for i in range(n):
    ptr = sh[i] + 1
    while ptr < 10 and cnt2[ptr] == 0:
        ptr += 1
    if ptr != 10:
        new_mor[i] = ptr
        cnt2[ptr] -= 1
    else:
        ptr = 0
        while ptr < 10 and cnt2[ptr] == 0:
            ptr += 1
        new_mor[i] = ptr
        cnt2[ptr] -= 1
for i in range(n):
    if new_mor[i] > sh[i]:
        gives += 1
print(takes, gives, sep='\n')
