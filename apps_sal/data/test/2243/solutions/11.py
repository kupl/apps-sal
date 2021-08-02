import heapq
from queue import PriorityQueue
import operator as op
3


class StdReader:
    def read_int(self):
        return int(self.read_string())

    def read_ints(self, sep=None):
        return [int(i) for i in self.read_strings(sep)]

    def read_float(self):
        return float(self.read_string())

    def read_floats(self, sep=None):
        return [float(i) for i in self.read_strings(sep)]

    def read_string(self):
        return input()

    def read_strings(self, sep=None):
        return self.read_string().split(sep)


reader = StdReader()


def main():
    n, k, q = reader.read_ints()
    t = reader.read_ints()

    # queue = PriorityQueue()
    queue = []
    qsize = 0

    # online = [False]*n
    # online_n = 0
    # prior = sorted([(i, t[i]) for i in range(n)], key=op.itemgetter(1), inverse=True)
    # pos = [0]*n
    # for i, p in enumerate(prior):
    # 	pos[p[0]] = i

    for i in range(q):
        qt, qid = reader.read_ints()
        qid -= 1

        if qt == 1:
            # qid online
            # online[qid] = True
            # online_n += 1
            if len(queue) == k:
                # queue.get()
                # heapq.heappop(queue)
                # qsize -= 1
                heapq.heappushpop(queue, (t[qid], qid))
            else:
                heapq.heappush(queue, (t[qid], qid))

            # queue.put((t[qid], qid))
            # heapq.heappush(queue, )
            # qsize += 1
        else:
            # query qid
            box = [i[1] for i in queue]
            # print(box)
            if qid in box:
                print('YES')
            else:
                print('NO')

            # if not online[qid]:
            # 	print('NO')
            # else:
            # 	pass


def __starting_point():
    main()


__starting_point()
