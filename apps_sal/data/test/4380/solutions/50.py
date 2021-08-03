a = list(map(int, input().split()))
set_a_b = set(a)
even_count = 0
for i in set_a_b:
    if i % 2 == 0:
        even_count += 1

if even_count == 0:
    print('Yes')
else:
    print('No')
