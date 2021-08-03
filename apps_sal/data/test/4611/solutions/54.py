import sys
N = int(input())
d = [list(map(int, input().split())) for l in range(N)]
d.insert(0, [0, 0, 0])
# print(N)
# print(d)


def get_length(l1, l2):
    return abs(l1[1] - l2[1]) + abs(l1[2] - l2[2])


for cnt in range(N):
    length = get_length(d[cnt], d[cnt + 1])
    time = abs(d[cnt][0] - d[cnt + 1][0])
    if length <= time and abs(time - length) % 2 == 0:
        pass
    else:
        print("No")
        return

print("Yes")
