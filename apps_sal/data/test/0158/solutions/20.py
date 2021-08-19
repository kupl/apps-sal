def main():
    nbEquipe = int(input())
    liste = list(map(int, input().split()))
    liste.sort()
    if liste[nbEquipe] > liste[nbEquipe - 1]:
        print('YES')
    else:
        print('NO')


main()
