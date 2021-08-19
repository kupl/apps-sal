n = int(input())
l = [int(i) for i in input().split(' ')]
one = l.count(1)
two = n - one
result = 0
if two >= one:
    result = one
else:
    result += two
    one = one - two
    result += int(one / 3)
print(result)
