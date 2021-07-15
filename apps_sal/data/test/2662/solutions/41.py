import bisect

n = int(input())
a = []

for i in range(n):
    x = int(input())
    a.append(x)
a = a[::-1]

stack = [a[0]]

for i in range(1, n):
    index = bisect.bisect_right(stack, a[i])
    if index == len(stack):
        stack.append(a[i])
    else:
        stack[index] = a[i]

print((len(stack)))

