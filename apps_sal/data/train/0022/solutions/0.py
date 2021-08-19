import sys
input = sys.stdin.readline
for _ in range(int(input())):
    (a, k) = list(map(int, input().split()))
    for _ in range(k - 1):
        if '0' in str(a):
            break
        a += int(min(list(str(a)))) * int(max(list(str(a))))
    print(a)
