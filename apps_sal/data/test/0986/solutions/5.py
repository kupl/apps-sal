def R():
    return map(int, input().split())


stack = []
(n, k) = R()
l = list(R())
(curr, tot) = (0, 0)
for i in range(n):
    if l[i] not in stack:
        if curr < k:
            curr = curr + 1
        else:
            (c, z) = (0, -1)
            for j in range(k):
                if stack[j] not in l[i:]:
                    z = j
                    break
                else:
                    c = max(c, i + l[i:].index(stack[j]))
            stack.pop(z) if z != -1 else stack.remove(l[c])
        stack.insert(0, l[i])
        tot += 1
print(tot)
