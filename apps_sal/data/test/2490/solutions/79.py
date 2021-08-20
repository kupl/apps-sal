n = input()
l = len(n)
(a, b) = (0, 1)
for v in n:
    v = int(v)
    a_next = min(a + v, b + (10 - v))
    b_next = min(a + v + 1, b + (10 - (v + 1)))
    a = a_next
    b = b_next
print(a)
