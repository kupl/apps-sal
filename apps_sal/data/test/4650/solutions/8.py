def main():
    for i in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        thr = 0
        tw = 0
        on = 0
        for val in a:
            if val % 3 == 0:
                thr += 1
            elif val % 3 == 2:
                tw += 1
            else:
                on += 1
        if tw == on:
            print(thr + tw)
        elif tw > on:
            print(thr + on + (tw - on) // 3)
        else:
            print(thr + tw + (on - tw) // 3)


main()
