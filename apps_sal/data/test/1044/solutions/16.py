def main():
    n = int(input())
    t = list(map(int, input().split()))
    somme = 0
    for i in range(len(t)):
        somme += t[i] - 1
        if somme % 2 == 0:
            print(2)
        else:
            print(1)


main()
