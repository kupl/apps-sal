n = int(input())
for _ in range(n):
    k = int(input())
    pos = [0] * k
    arr = list(map(int, input().split(' ')))
    for i in range(k):
        pos[arr[i] - 1] = i
    (left, right) = ([0] * k, [0] * k)
    (left[0], right[0]) = (pos[0], pos[0])
    for i in range(1, k):
        left[i] = min(left[i - 1], pos[i])
        right[i] = max(right[i - 1], pos[i])
    for i in range(k):
        if right[i] - left[i] == i:
            print(1, end='')
        else:
            print(0, end='')
    print()
