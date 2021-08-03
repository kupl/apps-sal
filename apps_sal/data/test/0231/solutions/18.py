def run(n, a):
    result = 1
    if a % 2 == 1:
        result += (a - 1) / 2
    else:
        result += (n - a) / 2

    print(int(result))


data = [int(x) for x in input().split(' ')]
run(n=data[0], a=data[1])
