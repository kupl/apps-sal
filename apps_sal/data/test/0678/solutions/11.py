n = int(input())
A = []
sum = 0
for i in range(n):
    x = int(input())
    sum += x
    A.append(sum/(i+1))

print('%.6f\n' % max(A))
