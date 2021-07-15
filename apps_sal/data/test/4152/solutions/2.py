n = int(input())
a = list(map(int, input().split()))
b = [1]
x = 1
for i in range(64):
    b.append(x * 2)
    x *= 2

dict = {}
ans = 0

for i in a:
    try:
        if dict[i] > 0:
            dict[i] += 1
    except KeyError:
        dict[i] = 1


for i in a:
    tmp = 0
    for j in b:
        try:
            if i == j - i and dict[i] < 2:
                pass
            elif j - i > 0 and dict[j - i]:
                tmp = 0
                break
        except KeyError:
            tmp = 1
    ans += tmp

print(ans)
