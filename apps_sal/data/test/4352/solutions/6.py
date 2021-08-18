
input_alice, input_bob = list(map(int, input().split()))

result = 'ret'

if input_alice > input_bob:
    if input_bob == 1:
        result = 'Bob'
    else:
        result = 'Alice'
elif input_alice < input_bob:
    if input_alice == 1:
        result = 'Alice'
    else:
        result = 'Bob'
else:
    result = 'Draw'

print(result)
