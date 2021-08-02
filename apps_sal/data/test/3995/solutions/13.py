n, k = list(map(int, input().split()))
e = (n - k) // 2
c = "0" * e + "1"
while(len(c) <= n):
    c = c + c
print(c[:n])
