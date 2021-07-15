def main(n,a):
    a = ("{:0"+ ("{}".format(n)) + "d}").format(int(a))
    mn = int(a)
    for j in range(n):
        x = list(a[j:]+a[:j])
        y = x.copy()
        #for i in range(10):
        i = 10-int(y[0])
        x = y.copy()
        for k in range(n):
            x[k] = str((int(x[k])+i)%10)
        #print(j,i,x, mn)
        if int("".join(x)) < mn:
            mn = int("".join(x))

    print(("{:0"+ ("{}".format(n)) + "d}").format(mn))


def main_input():
    n = int(input())
    a = int(input())
    main(n,a)

def __starting_point():
    main_input()

__starting_point()
