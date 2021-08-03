n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_odd, a_even, b_odd, b_even = 0, 0, 0, 0

for i in a:
    if i % 2 == 0:
        a_even += 1
    else:
        a_odd += 1

for i in b:
    if i % 2 == 0:
        b_even += 1
    else:
        b_odd += 1

print(min(a_odd, b_even) + min(a_even, b_odd))
