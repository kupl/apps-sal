def main():
    n, k = map(int, input().split())
    beauty = list(map(int, input().split()))
    capitals = set(map(int, input().split()))
    result = balans = 0
    for i in range(n):
        if ((i + 1) not in capitals) and ((i + 1) % n) + 1 not in capitals:
            balans = beauty[i] * beauty[(i + 1) % n]
            result += balans
    balans = sum(beauty)
    for i in capitals:
        balans -= beauty[i - 1]
        result += balans * beauty[i - 1]
    print(result)


main()
