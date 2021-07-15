from collections import Counter

n = int(input().strip())
ca = Counter([int(x) for x in input().strip().split(' ')])
cb = Counter([int(x) for x in input().strip().split(' ')])
cnt = 0

for i in range(1, 6):
    if (ca[i] + cb[i]) % 2 != 0:
        print(-1)
        return
    else:
        cnt += abs(ca[i] - (ca[i] + cb[i]) / 2)
print(int(cnt/2))

