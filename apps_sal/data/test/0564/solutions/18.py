(n, s) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
result = 'NO'
m = max(a)
if sum(a) - m <= s:
    result = 'YES'
print(result)
