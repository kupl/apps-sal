class TupleHeap(object):
    def __init__(self):
        self.heap = [0]

    def mult(self, i):
        return self.heap[i][0] * self.heap[i][1]

    def __str__(self):
        return " ".join(map(str, self.heap))

    def add(self, var):
        self.heap.append(var)
        if len(self.heap) > 2:
            el = len(self.heap) - 1
            par = el // 2
            while (el != 1) and (self.mult(el) > self.mult(par)):
                self.heap[el], self.heap[par] = self.heap[par], self.heap[el]
                el = par
                par = el // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        ans = self.heap[1]
        if len(self.heap) == 2:
            self.heap.pop()
            return ans
        self.heap[1] = self.heap.pop()
        el = 1
        var_el = self.mult(el)
        child1 = el * 2
        if child1 < len(self.heap):
            var_child1 = self.mult(child1)
        else:
            var_child1 = -1
        child2 = el * 2 + 1
        if child2 < len(self.heap):
            var_child2 = self.mult(child2)
        else:
            var_child2 = -1
        while (var_child2 > var_el) or (var_child1 > var_el):
            if var_child1 > var_child2:
                self.heap[el], self.heap[child1] = self.heap[child1], self.heap[el]
                el = child1
            else:
                self.heap[el], self.heap[child2] = self.heap[child2], self.heap[el]
                el = child2
            var_el = self.mult(el)
            child1 = el * 2
            if child1 < len(self.heap):
                var_child1 = self.mult(child1)
            else:
                var_child1 = -1
            child2 = el * 2 + 1
            if child2 < len(self.heap):
                var_child2 = self.mult(child2)
            else:
                var_child2 = -1
        return ans


n, m, r, k = map(int, input().split())

max_x = min(r, n - r + 1)
max_y = min(r, m - r + 1)
col_max_x = n - 2 * (max_x - 1)
col_max_y = m - 2 * (max_y - 1)
Nr = (n - r + 1) * (m - r + 1)


tuple_heap = TupleHeap()
tuple_heap.add((max_x, max_y))
used = {(max_x, max_y)}
SUMM = 0

curr = tuple_heap.pop()
while (curr is not None) and (curr[0] > 0) and (curr[1] > 0) and (k > 0):
    new_tuple1 = (curr[0] - 1, curr[1])
    if new_tuple1 not in used:
        used.add(new_tuple1)
        tuple_heap.add(new_tuple1)
    new_tuple2 = (curr[0], curr[1] - 1)
    if new_tuple2 not in used:
        used.add(new_tuple2)
        tuple_heap.add(new_tuple2)
    x = 2 if curr[0] != max_x else col_max_x
    y = 2 if curr[1] != max_y else col_max_y
    col = min(x * y, k)
    k = k - col
    SUMM = SUMM + col * curr[0] * curr[1]
    curr = tuple_heap.pop()

print(SUMM / Nr)
