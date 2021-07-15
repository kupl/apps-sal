class IntegersFun():
    def __init__(self, n):
        self.n = n

    def get_value(self):
        sm = 0
        for i in range(2,self.n+1):
            for j in range(2*i, self.n+1, i):
                sm += 4*j/i
        return int(sm)

n = int(input())
print(IntegersFun(n).get_value())
