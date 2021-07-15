
class SegmentTree:

    @classmethod
    def all_identity(cls, operator, equality, identity, size):
        return cls(operator, equality, identity, [identity]*(2 << (size-1).bit_length()))

    @classmethod
    def from_initial_data(cls, operator, equality, identity, data):
        size = 1 << (len(data)-1).bit_length()
        temp = [identity]*(2*size)
        temp[size:size+len(data)] = data
        data = temp

        for i in reversed(range(size)):
            data[i] = operator(data[2*i],data[2*i+1])
        return cls(operator, equality, identity, data)

    def __init__(self, operator, equality, identity, data):
        if equality is None:
            equality = lambda a,b: False
        self.op = operator
        self.eq = equality
        self.id = identity
        self.data = data
        self.size = len(data)//2

    def _interval(self, a, b):
        a += self.size
        b += self.size
        ra = self.id
        rb = self.id

        data = self.data
        op = self.op
        while a < b:
            if a & 1:
                ra = op(ra,data[a])
                a += 1
            if b & 1:
                b -= 1
                rb = op(data[b],rb)
            a >>= 1
            b >>= 1
        return op(ra,rb)

    def __getitem__(self, i):
        if isinstance(i, slice):
            return self._interval(
                                    0 if i.start is None else i.start,
                                    self.size if i.stop is None else i.stop)
        elif isinstance(i, int):
            return self.data[i+self.size]

    def __setitem__(self, i, v):
        i += self.size
        data = self.data
        op = self.op
        eq = self.eq
        while i and not eq(data[i],v):
            data[i] = v
            v = op(data[i^1],v) if i & 1 else op(v,data[i^1])
            i >>= 1

    def __iter__(self):
        return self.data[self.size:]


def solve(A,B):
    from operator import eq

    N = len(B)

    counts = [0]*N
    for b in B:
        counts[b] += 1

    init_data = [i if counts[i] > 0 else N for i in range(N)]

    seg = SegmentTree.from_initial_data(min, eq, N, init_data)

    def it():
        for a in A:
            best_b = -a%N

            p = seg[best_b:]
            if p == N:
                p = seg[:best_b]
            counts[p] -= 1
            if counts[p] == 0:
                seg[p] = N
            yield (a+p)%N
    return tuple(it())



def main():
    input()
    A = tuple(map(int,input().split()))
    B = list(map(int,input().split()))

    res = solve(A,B)
    print(*res)

main()
