def main():
    n = int(input())
    a = [int(s) for s in input().split()]
    if a[-1] == 15:
        print('DOWN')
        return
    if a[-1] == 0:
        print('UP')
        return
    if n == 1:
        print(-1)
        return
    if a[-2] < a[-1]:
        print('UP')
        return
    else:
        print('DOWN')
        return


main()
