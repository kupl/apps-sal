import itertools
N = int(input())
cnt = 0
for i in range(3, len(str(N)) + 1):
    for j in list(itertools.product('357', repeat=i)):
        if ('3' in j) & ('5' in j) & ('7' in j):
            if int(''.join(j)) <= N:
                cnt += 1
            else:
                break
print(cnt)
