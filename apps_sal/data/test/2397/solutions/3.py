
def main():
    buf = input()
    buflist = buf.split()
    n = int(buflist[0])
    k = int(buflist[1])
    buf = input()
    buflist = buf.split()
    a = list(map(int, buflist))
    a_sum = []
    for i in range(1, len(a)+1):
        if not a_sum:
            a_sum.append(a[-i])
        else:
            a_sum.append(a[-i]+a_sum[-1])
    cost = a_sum.pop()
    a_sum.sort(reverse=True)
    for i in range(k-1):
        cost += a_sum[i]
    print(cost)

def __starting_point():
    main()

__starting_point()
