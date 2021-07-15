# coding=utf-8

def __starting_point():
    A, B = list(map(int, input().split()))

    ans = -1
    while(ans*0.08 < A or ans*0.1 < B):
        ans += 1


    if int(ans * 0.08) == A and int(ans * 0.1) == B:
        print(ans)

    else:
        print('-1')

    #print(ans, ans*0.08, ans*0.1)

__starting_point()
