n = int(input())
aa = list(map(int, input().split()))
if n % 2 == 0:
    a = aa[n - 1:0:-2] + aa[0:n - 1:2]
else:
    a = aa[n - 1::-2] + aa[1:n - 1:2]
print(*a)
