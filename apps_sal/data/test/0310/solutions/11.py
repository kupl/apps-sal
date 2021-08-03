n, k = list(map(int, input().split()))
s = k // n
if k % n != 0:
    s += 1
print(s)
