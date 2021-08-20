import sys
input = sys.stdin.readline


def RI():
    return [int(x) for x in sys.stdin.readline().strip().split()]


def rw():
    return input().strip().split()


infinite = float('inf')
t = int(input())
for _ in range(t):
    (n, k) = RI()
    s = input()
    mini = n
    test = 'RGB' * (k // 3 + 5)
    for i in range(n - k + 1):
        count = 0
        for j in range(k):
            if s[i + j] != test[j]:
                count += 1
        mini = min(count, mini)
    test = 'GBR' * (k // 3 + 5)
    for i in range(n - k + 1):
        count = 0
        for j in range(k):
            if s[i + j] != test[j]:
                count += 1
        mini = min(count, mini)
    test = 'BRG' * (k // 3 + 5)
    for i in range(n - k + 1):
        count = 0
        for j in range(k):
            if s[i + j] != test[j]:
                count += 1
        mini = min(count, mini)
    print(mini)
