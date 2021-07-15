import sys


class main:

    def __init__(self):
        self.n=int(sys.stdin.readline())

        self.line=dict()
        for i in range(self.n):
            a,b=(int(s) for s in sys.stdin.readline().rstrip().split(' '))
            self.line[a]=self.line.get(a,0)+1
            self.line[b+1]=self.line.get(b+1,0)-1

    def calc(self):
        self.result=dict()
        sorted_keys = sorted(self.line.keys())

        count=0
        last=sorted_keys[0]
        for k in sorted_keys:
            self.result[count]=self.result.get(count,0)+k-last
            count=count+self.line[k]
            last=k
        del self.result[0]

    def out(self):
        for k in range(1,self.n):
            print(self.result.get(k,0),end=' ')
        print(self.result.get(self.n, 0), end='')

    def solve(self):
        self.calc()
        self.out()


def __starting_point():
    m=main()
    m.solve()
    pass

__starting_point()
