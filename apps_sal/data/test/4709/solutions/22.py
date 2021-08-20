(a, op, b) = list(map(str, input().split()))
input_a = int(a)
input_b = int(b)
result = 0
if op == '+':
    result = input_a + input_b
elif op == '-':
    result = input_a - input_b
else:
    result = 'Error'
print(result)
