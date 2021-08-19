v = []
(n, k) = list(map(int, input().split()))
s = 0
v = [int(x) for x in input().split()]
q = 0
carry = 0
for i in range(len(v)):
    prev_carry = carry
    garbage = v[i] + carry
    boxes = garbage // k
    carry = garbage % k
    if i > 0 and boxes == 0 and (carry > 0) and (prev_carry > 0):
        carry = 0
        boxes = 1
    q += boxes
if carry > 0:
    q += 1
print(q)
