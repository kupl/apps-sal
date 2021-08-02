def solve(n, a):
    a = sorted(a)
    col = [False for i in range(n)]
    count = 0
    for i in range(n):
        if not col[i]:
            count += 1
            col[i] = True
            for j in range(n):
                if a[j] % a[i] == 0:
                    col[j] = True
    return count


n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
