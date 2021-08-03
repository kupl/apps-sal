def main():
    s = input()
    n = list(s)
    n.sort()
    k = 0
    f = 0
    i = 0
    while(i < len(s)):
        if(n.count(n[i]) == 1 and f == 0):
            f = 1

        else:
            if(n.count(n[i]) % 2 != 0):
                k = k + n.count(n[i])

        i = i + n.count(n[i])

    if(k == 0):
        print("First")
        return
    if(f == 0):
        if(k % 2 != 0):
            print("First")
            return
        else:
            print("Second")
            return
    else:
        if(k % 2 == 0):
            print("First")
            return
        else:
            print("Second")
            return


main()
