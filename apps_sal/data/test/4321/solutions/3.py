def minus(s):
    if s % 10 == 0:
        return s // 10
    else:
        return s - 1


(n, k) = map(int, input().split())
for i in range(k):
    n = minus(n)
print(n)
