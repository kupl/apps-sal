a = list(input())[::-1]
b = list(input())[::-1]
c = list(input())[::-1]

abc = [a, b, c]
num1 = {'a': 0, 'b': 1, 'c': 2}
num2 = ['A', 'B', 'C']
d = 0
while True:
    if abc[d]:
        d = num1[abc[d].pop()]
    else:
        break
print(num2[d])
