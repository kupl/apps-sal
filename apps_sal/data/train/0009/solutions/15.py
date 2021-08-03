import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x = input().rstrip()

    arr = []

    c = 0
    for char in x:
        if char == '1':
            c += 1
        else:
            arr.append(c)
            c = 0

    arr.append(c)
    arr.sort()
    arr.reverse()

    ans = 0
    for i in range(0, len(arr), 2):
        ans += arr[i]

    print(ans)
