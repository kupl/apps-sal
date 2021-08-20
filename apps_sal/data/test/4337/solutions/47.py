N = int(input())
s = list(map(str, input().split()))
result = 'Three'
if s.count('Y') > 0:
    result = 'Four'
print(result)
