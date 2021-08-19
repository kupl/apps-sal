(n, m, k) = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
delt = []
for i in range(1, len(b)):
    a = b[i] - b[i - 1] - 1
    delt.append(a)
counter = b[-1] - b[0] + 1
delt.sort(reverse=True)
for item in delt:
    if k <= 1:
        break
    counter -= item
    k -= 1
print(counter)
