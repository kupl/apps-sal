a = []
was_already = was_twice = 0
n = int(input().split()[0])
for _ in range(n):
    ai = int(input(), base=2)
    a.append(ai)
    was_twice |= was_already & ai
    was_already |= ai
for ai in a:
    if ai & (ai ^ was_twice):
        continue
    print('YES')
    break
else:
    print('NO')
