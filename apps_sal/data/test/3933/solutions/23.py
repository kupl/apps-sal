def solve():
    dias = int(input())
    numbers = list([int(x) for x in input().split(' ')])
    diferencia = numbers[1] - numbers[0]
#	print('diferencia', diferencia)
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] == diferencia:
            continue
        else:
            print(numbers[len(numbers) - 1])
            return
    print(numbers[len(numbers) - 1] + diferencia)


while True:
    try:
        solve()
    except:
        break
