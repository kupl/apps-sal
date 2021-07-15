import time

def find_max_clique(remain, size, max_, index, maxs):
    # print(remain, size, max_)
    result = max_
    if size + len(remain) <= result:
        # print('pruning (1)...')
        return result
    if not remain:
        # print('trivial')
        return size
    while remain:
        candidate = max(remain)
        # print('get candidate:', candidate)
        if maxs[candidate] + size <= result:
            # print('pruning (2)...')
            return result
        if size + len(remain) <= result:
            # print('pruning (3)...')
            return result
        remain.remove(candidate)
        # print('entering...')
        sub_result = find_max_clique(remain & index[candidate], size + 1 , result, index, maxs)
        if sub_result > result:
            # print('{} > {}, existing...'.format(sub_result, result))
            result = sub_result
            return result
    # print('result:', result)
    return result

def test_find():
    # index = {1: {2, 3, 4}, 2: {1, 3, 4}, 3: {1, 2}, 4: {1, 2}}
    index = [{2, 4, 5, 7}, {4, 5, 6}, {0, 5, 6, 7},
        {5, 6 ,7}, {0, 1, 6, 7}, {0, 1, 2, 3}, {1, 2, 3, 4},
        {0, 2, 3, 4}]
    m = 8
    maxs = [0] * m
    whole = set()
    for i in range(m):
        # print('i:', i)
        whole.add(i)
        # print('w:', whole)
        maxs[i] = max(maxs[i - 1], find_max_clique(whole & index[i], 1, maxs[i - 1], index, maxs))
        # print()
    # print(maxs)

def solve(events, m):
    index = [set() for _ in range(m)]
    r = []
    while events:
        ele = events.pop()
        if ele is None:
            # ele is None
            r.clear()
        else:
            # ele not None.
            for n in r:
                index[n].add(ele)
            index[ele].update(r)
            r.append(ele)
    whole = set(range(m))
    # print('w:', whole)
    for i in range(m):
        index[i] = whole - index[i] - {i}
    maxs = [0] * m
    whole = set()
    for i in range(m):
        whole.add(i)
        maxs[i] = max(maxs[i - 1], find_max_clique(whole & index[i], 1, maxs[i - 1], index, maxs))
    return maxs[-1]


def test():
    events = []
    m = 700
    for i in range(m):
        events.extend([None, i])
    tick = time.time()
    print(solve(events, m))
    tock = time.time()
    print('T:', round(tock - tick, 5)) 
    
def main():
    # Deal input here.
    n, m = list(map(int, input().split()))
    events = []
    d = {}
    id_ = 0
    for i in range(n):
        line = input()
        if line.startswith('1'):
            events.append(None)
        else:
            if line not in d:
                d[line] = id_
                id_ += 1
            events.append(d[line])
    
    # tick = time.time()
    print(solve(events, m))
    # tock = time.time()
    # print(round(tock - tick, 5))


def __starting_point():
    main()

__starting_point()
