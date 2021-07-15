n, B = list(map(int, input().split()))
a = list(map(int, input().split()))

def solve(a, B):
    diff, k = [], 0
    for i in range(0, len(a)-1):
        if a[i] % 2 == 0: k += 1
        else: k -= 1
        if k == 0:
            diff.append(abs(a[i+1] - a[i]))
    diff.sort()
    s = 0
    for i in range(len(diff)):
        s += diff[i]
        if s > B:return i
    return len(diff)

print(solve(a, B))
