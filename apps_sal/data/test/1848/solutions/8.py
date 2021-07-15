n = int(input())
count = [0] * 1001
c = [0] * 1001
pictures = list(map(int, input().split()))
for i in pictures:
    count[i] += 1
res = 0
while count != c:
    res -= 1
    for i in range(len(count)):
        if count[i] > 0:
            count[i] -= 1
            res += 1
print(res)
