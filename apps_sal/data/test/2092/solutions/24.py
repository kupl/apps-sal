class Traps():
    def __init__(self,l,r,d):
        self.before_l = l - 1
        self.r = r
        self.d = d

def qujianbingji(x,y):
    if y[0]<x[0]:
        if y[1]<x[0]:
            return [y,x]
        elif y[1]<=x[1]:
            z = [y[0],x[1]]
            return [z]
        else:
            return [y]
    elif y[0]<x[1]:
        if y[1]<=x[1]:
            return [x]
        else:
            z = [x[0],y[1]]
            return [z]
    else:
        return [x,y]


def main():
    m, n, k, t = map(int, input().split())
    lista = list(map(int, input().split()))
    lista.sort(reverse=True)
    list_traps = []
    for i in range(k):
        l, r, d = map(int, input().split())
        list_traps.append(Traps(l,r,d))
    list_traps.sort(key=lambda x:x.before_l)
    T = 0
    left, right = -1, m
    while right-left>1:#？？？？？？？
        dangerous_traps = []
        mid = (left+right)//2

        for trap in list_traps:
            if trap.d > lista[mid]:
                dangerous_traps.append(trap)

        if dangerous_traps == []:
            T = n + 1
        else:
            space = 0
            finalbing = [[dangerous_traps[0].before_l, dangerous_traps[0].r]]
            for dangerous_trap in dangerous_traps:
                c = qujianbingji(finalbing[-1], [dangerous_trap.before_l, dangerous_trap.r])
                del finalbing[-1]
                if len(c) == 2:
                    finalbing.append(c[0])
                    finalbing.append(c[1])
                else:
                    finalbing.append(c[0])
            lenfb = len(finalbing)
            if lenfb == 1:
                T = n + 1 + (finalbing[0][1] - finalbing[0][0]) * 2
            else:
                for x in range(lenfb - 1):
                    space += finalbing[x + 1][0] - finalbing[x][1]
                maxlen = finalbing[-1][1] - finalbing[0][0]
                T = n + 1 + 2 * (maxlen - space)

        if T > t:
            left, right = left, mid
            count = mid

        else:
            left, right = mid, right
            count = mid + 1
    print(count)

    # for i in range(0,m):
    #
    #     dangerous_traps = []
    #     list_r = []
    #     list_l = []
    #     for trap in list_traps:
    #         if trap.d > lista[i]:
    #             dangerous_traps.append(trap)
    #             list_r.append(trap.r)
    #             list_l.append(trap.before_l)
    #     if dangerous_traps == []:
    #         T = n+1
    #     else:
    #         space = 0
    #         lenth = len(dangerous_traps)
    #         finalbing = [[dangerous_traps[0].before_l,dangerous_traps[0].r]]
    #         for dangerous_trap in dangerous_traps:
    #             c = qujianbingji(finalbing[-1],[dangerous_trap.before_l,dangerous_trap.r])
    #             del finalbing[-1]
    #             if len(c)==2:
    #                 finalbing.append(c[0])
    #                 finalbing.append(c[1])
    #             else:
    #                 finalbing.append(c[0])
    #         lenfb =len(finalbing)
    #         if lenfb == 1:
    #             T = n+1 + (finalbing[0][1]-finalbing[0][0])*2
    #         else:
    #             for x in range(lenfb-1):
    #                 space += finalbing[x+1][0]-finalbing[x][1]
    #             maxlen = finalbing[-1][1]-finalbing[0][0]
    #             T = n + 1 + 2 * (maxlen - space)
    #
    #     if T > t:
    #         left, right = mid,right
    #         count = i
    #     else:
    #         left,right = left, mid
    #         count = i+1
    # print(count)

main()
