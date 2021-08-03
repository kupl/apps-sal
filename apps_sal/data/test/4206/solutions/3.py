def main():
    ret = 0
    lst = [int(i) for i in input()]
    l = len(lst)
    ind = 0
    while ind < l:
        if lst[ind] % 3 == 0:
            ind += 1
            ret += 1
        elif l - ind >= 2 and ((lst[ind] + lst[ind + 1]) % 3 == 0 or lst[ind + 1] % 3 == 0):
            ret += 1
            ind += 2
        elif l - ind >= 3 and ((lst[ind] + lst[ind + 1] + lst[ind + 2]) % 3 == 0 or (lst[ind + 1] + lst[ind + 2]) % 3 == 0 or lst[ind + 2] % 3 == 0):
            ret += 1
            ind += 3
        else:
            break
    print(ret)
    return 0


main()
