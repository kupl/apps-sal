import sys


def main():
    x = sys.stdin.readline().split()
    n, m = int(x[0]), int(x[1])
    
    k = int(n/5)
    rest = n - k*5
    a = [k]*5
    for i in range(rest):
        a[i+1]+=1

    k = int(m/5)
    rest = m - k*5
    b = [k]*5
    for i in range(rest):
        b[i+1]+=1

    r = a[0]*b[0] + a[1]*b[4] + a[2]*b[3]+ a[3]*b[2] + a[4]*b[1]

    print(r)

main()

