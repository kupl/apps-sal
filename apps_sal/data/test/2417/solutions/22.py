n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
op = [0] * (n + 1)
i = 0
j = 0
while i < n and j < n:
    if a[i] == b[j]:
        i += 1
        while i < n and op[a[i]] == 1:
            i += 1
        j += 1
    else:
        op[b[j]] = 1
        j += 1
print(sum(op))
