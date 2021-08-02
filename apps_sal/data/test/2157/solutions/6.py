import sys
data = [int(i) for i in sys.stdin.read().split()]
data.reverse()

n1, n2 = data.pop(), data.pop()
a = sorted([data.pop() for i in range(n1)], reverse=True)

# n = list(map(int,input().split()))
# a = sorted(list(map(int,input().split())),reverse=True)
check = [0] * (n1 + 1)  # Массив для указателей на отметки, между которыми происходит заполнение
result = [0] * n1  # Массив содержащий лучшее расположение элементов
for i in range(n2):
    temp1, temp2 = data.pop(), data.pop()
    check[temp1 - 1] += 1  # Указатели на отметки для заполнения
    check[temp2] -= 1
temp = 0
for i in range(n1):
    temp += check[i]
    result[i] = temp
result.sort(reverse=True)
sum = 0
for i in range(n1): sum += result[i] * a[i]
print(sum)
