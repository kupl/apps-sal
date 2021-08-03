n = int(input())
l = list(map(int, input().split()))
nl = [-1] * n
keys = 0
turns = 0
# print(l)
# print("BEGIN-----------------")
while l != nl:
    if turns % 2 == 0:
        for pos in range(n):
            if l[pos] <= keys and l[pos] != -1:
                keys += 1
                l[pos] = -1
    else:
        for pos in range(n - 1, -1, -1):
            if l[pos] <= keys and l[pos] != -1:
                keys += 1
                l[pos] = -1
    # print(l)
    turns += 1
print(turns - 1)
