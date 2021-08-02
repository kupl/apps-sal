# cook your dish here

n, k = map(int, input().split())

i = 0
while i < k:
    if str(n)[-1] != '0':
        n = n - 1
    else:
        n = n // 10
    i = i + 1
print(n)
