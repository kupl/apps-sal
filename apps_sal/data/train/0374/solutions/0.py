class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        A = [a for i, a in enumerate(A) if all(a not in b for j, b in enumerate(A) if i != j)]

        def memo(f):
            dic = {}

            def f_alt(*args):
                if args not in dic:
                    dic[args] = f(*args)
                return dic[args]
            return f_alt

        def merge(w1, w2):
            for k in range(len(w2), -1, -1):
                if w1.endswith(w2[:k]):
                    return w1+w2[k:]

        @memo
        def find_short(tup, last):
            if len(tup) == 1:
                return A[tup[0]]
            mtup = tuple(t for t in tup if t != last)
            return min((merge(find_short(mtup, t), A[last]) for t in mtup), key=len)

        tup = tuple(range(len(A)))

        return min((find_short(tup, i) for i in range(len(A))), key=len)

