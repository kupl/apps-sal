def main():
    N, K = map(int, input().split())
    A_list = list(map(str, input().split()))
    use_list = ["0","1","2","3","4","5","6","7","8","9"]
    list_A = list(set(use_list) - set(A_list))
    #print("list_A", list_A)
    for i in range(100000) :
        ans = N + i
        #print("ans", ans)
        ans_str = str(ans)
        frag = 0
        for val in ans_str :
            #print("val", val)
            if str(val) in list_A :
                pass
                #print("frag", frag)
            else :
                frag = 1
                break

        if frag == 0 :
            break
    print(ans)


def __starting_point():
    main()
__starting_point()
