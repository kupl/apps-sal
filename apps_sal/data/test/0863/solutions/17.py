(a, ta) = map(int, input().split())
(b, tb) = map(int, input().split())
sl = input().split(':')
s = 60 * int(sl[0]) + int(sl[1])
print(sum((1 for i in range(5 * 60, 24 * 60, b) if i < s + ta and i + tb > s)))
