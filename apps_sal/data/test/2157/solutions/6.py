import sys
data = [int(i) for i in sys.stdin.read().split()]
data.reverse()

n1, n2 = data.pop(), data.pop()
a = sorted([data.pop() for i in range(n1)], reverse=True)

check = [0] * (n1 + 1)
result = [0] * n1
for i in range(n2):
    temp1, temp2 = data.pop(), data.pop()
    check[temp1 - 1] += 1
    check[temp2] -= 1
temp = 0
for i in range(n1):
    temp += check[i]
    result[i] = temp
result.sort(reverse=True)
sum = 0
for i in range(n1):
    sum += result[i] * a[i]
print(sum)
