(n, k) = map(int, input().split())
length = (n - k + 2) // 2
string = '0' * (length - 1) + '1'
answer = string * (n // length + 1)
print(answer[:n])
