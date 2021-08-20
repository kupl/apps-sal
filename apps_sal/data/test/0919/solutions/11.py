def read():
    return int(input())


def readmap():
    return list(map(int, input().split()))


def readlist():
    return list(map(int, input().split()))


def ctoi(c):
    return ord(c) - 96


(n, k) = readmap()
S = input()
stage = [0] * 27
for s in S:
    stage[ctoi(s)] = 1
ans = 0
i = 1
while k > 0 and i < 27:
    if stage[i]:
        ans += i
        k -= 1
        i += 2
    else:
        i += 1
if k > 0:
    print(-1)
else:
    print(ans)
