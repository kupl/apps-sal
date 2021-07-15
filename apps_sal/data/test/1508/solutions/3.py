n = int(input())
A = list(map(int, input().split()))
x = max(A)
A.pop(A.index(max(A)))
y = min(A)
A.sort()
A.pop(A.index(min(A)))
print(' '.join(list(map(str, [x] + A + [y]))))

