import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    cum = [a[0]]
    for i in range(n - 1):
        cum.append(cum[i] + a[i + 1])
    cum.append(cum[-1])
    print(cum[k])
