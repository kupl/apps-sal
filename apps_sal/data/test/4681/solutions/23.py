n = int(input())
if n == 0:
    print(2)
    return
elif n == 1:
    print(1)
    return

q = [2, 1]
for i in range(2, 88):
    m = q[i - 1] + q[i - 2]
    q.append(m)

print(q[n])
