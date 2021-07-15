def main():
    w = str(input())
    wl = []
    for ww in w :
        wl.append(ww)
    if len(w) % 2 != 0 :
        ans = "No"
    else :
        ans = "Yes"
        for val in wl :
            if wl.count(val) % 2 == 0 :
                pass
            else :
                ans = "No"
                break
    print(ans)



def __starting_point():
    main()

__starting_point()
