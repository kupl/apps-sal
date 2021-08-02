t = int(input())
for T in range(t):
    n, m = list(map(int, input().strip().split()))
    v = list(map(int, input().strip().split()))
    u = [0] * n
    for i in list(map(int, input().strip().split())):
        u[i - 1] = 1
    for i in range(n):
        j = i
        while j > 0 and u[j - 1] and v[j] < v[j - 1]:
            v[j], v[j - 1] = v[j - 1], v[j]
            j -= 1
    if v == sorted(v): print("YES")
    else: print("NO")
