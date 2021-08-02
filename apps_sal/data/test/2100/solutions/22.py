n = int(input())
left = []
right = []

for i in range(n):
    l, r = input().split()

    left.append(l)
    right.append(r)

left_0 = left.count('0')
left_1 = left.count('1')
right_0 = right.count('0')
right_1 = right.count('1')

print(min(left_0, left_1) + min(right_0, right_1))
