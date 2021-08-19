t = int(input())
for _ in range(t):
    (a, b) = map(int, input().split())
    start = ord('a')
    for i in range(a):
        print(chr(start + i % b), end='')
    print()
