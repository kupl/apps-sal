def inN():
    return int(input())


def inL():
    return list(map(int, input().split()))


def inNL(n):
    return [list(map(int, input().split())) for i in range(n)]


s = input()
n = int(s)
l = len(s)
cnt = 0
mod = [0] * 2019
m = 0
for i in range(l):
    m = (int(s[l - 1 - i]) * pow(10, i, 2019) + m) % 2019
    mod[m] += 1

cnt += mod[0]

for i in range(2019):
    if mod[i] > 1:
        cnt += (mod[i] * (mod[i] - 1)) / 2
        # print(i)
print((int(cnt)))
