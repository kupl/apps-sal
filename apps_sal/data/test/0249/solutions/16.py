from collections import defaultdict


class LongJumps:

    def __init__(self, n, l, x, y, a):
        (self.n, self.l, self.x, self.y, self.a) = (n, l, x, y, a)

    def get_markers(self):
        st = defaultdict(set)
        req_pts = [self.x, self.y]
        exist_check = defaultdict(bool)
        value_check = defaultdict(bool)
        for v in self.a:
            exist_check[v] = True
        for v in self.a:
            for i in range(len(req_pts)):
                if v - req_pts[i] >= 0:
                    st[v - req_pts[i]].add(i)
                    if exist_check[v - req_pts[i]]:
                        value_check[i] = True
                if v + req_pts[i] <= l:
                    st[v + req_pts[i]].add(i)
                    if exist_check[v + req_pts[i]]:
                        value_check[i] = True
        if value_check[0] and value_check[1]:
            print(0)
            return
        sol_status = 2
        status1_marker = None
        for v in st:
            if len(st[v]) == 2:
                sol_status = 1
                status1_marker = v
            elif len(st[v]) == 1:
                if exist_check[v]:
                    sol_status = 1
                    status1_marker = req_pts[1 - st[v].pop()]
        if sol_status == 1:
            print(1)
            print(status1_marker)
            return
        else:
            print(2)
            print(x, y)


(n, l, x, y) = list(map(int, input().strip(' ').split(' ')))
a = list(map(int, input().strip(' ').split(' ')))
lj = LongJumps(n, l, x, y, a)
lj.get_markers()
