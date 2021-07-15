def p(a):
    k = str(a)
    if (a // 10) == 0:
        k = '0' + k
    return k

def main():
    h, m = map(int, input().split(':'))
    h1, m1 = map(int, input().split(':'))
    k = (h * 60 + m + h1 * 60 + m1) // 2
    print(p(k // 60), p(k % 60), sep=':')
 
 
main()

