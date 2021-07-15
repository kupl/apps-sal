n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = sum(a)
B = sum(sorted(b)[-2:])

print(('NO', 'YES')[A <= B])

