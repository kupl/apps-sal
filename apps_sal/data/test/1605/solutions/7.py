s = input()
(ep, op, enp, onp) = (0, 0, 0, 0)
prev = ''
(totalE, totalO) = (0, 0)
for c in s:
    if prev == c:
        (ep, op, enp, onp) = (op, ep + 1, onp, enp)
    else:
        (ep, op, enp, onp) = (onp, 1 + enp, op, ep)
    (totalO, totalE) = (totalO + op, totalE + ep)
    prev = c
print(totalE, totalO)
