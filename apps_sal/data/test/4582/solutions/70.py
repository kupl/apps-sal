(input_a, input_b) = list(map(str, input().split()))
reslut = 'ret'
if input_a == 'H':
    if input_b == 'H':
        result = 'H'
    elif input_b == 'D':
        result = 'D'
elif input_a == 'D':
    if input_b == 'H':
        result = 'D'
    elif input_b == 'D':
        result = 'H'
else:
    reslut = "I don't Know."
print(result)
