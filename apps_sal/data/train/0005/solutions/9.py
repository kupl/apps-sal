import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    seen = [False] * (n+1)
    ans = set()
    for i, x in enumerate(a):
        if seen[x]:
            if sorted(a[:i]) == list(range(1, i+1)) and sorted(a[i:]) == list(range(1, n-i+1)):
                ans.add((i, n-i))
            break
        seen[x] = True
    seen = [False] * (n+1)
    for i, x in list(enumerate(a))[::-1]:
        if seen[x]:
            if sorted(a[:i+1]) == list(range(1, i+2)) and sorted(a[i+1:]) == list(range(1, n-i)):
                ans.add((i+1, n-i-1))
            break
        seen[x] = True
    print(len(ans))
    for l1, l2 in ans:
        print(l1, l2)


