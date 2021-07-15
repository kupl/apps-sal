def main():
    n  = int(input())
    s = list(input().split())
    hina = ['P','W','G','Y']
    hina_type = 0
    for i in hina:
        if i in s:
            hina_type += 1
    if hina_type == 3:
        print('Three')
    if hina_type == 4:
        print('Four')



def __starting_point():
    main()

__starting_point()
