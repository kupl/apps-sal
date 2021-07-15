
import heapq


def submit():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    def get(i, j, k):
        return a[i] + b[j] + c[k], (i, j, k)

    check = set()
    check.add((0, 0, 0))
    ans = [get(0, 0, 0)]
    q = []
    for _ in range(k - 1):
        prev, (i, j, k) = ans[-1]
        
        if i < x - 1:
            new_triple = (i + 1, j, k)
            if new_triple not in check:
                check.add(new_triple)
                s, _ = get(*new_triple)
                heapq.heappush(q, (-s, new_triple))
        
        if j < y - 1:
            new_triple = (i, j + 1, k)
            if new_triple not in check:
                check.add(new_triple)
                s, _ = get(*new_triple)
                heapq.heappush(q, (-s, new_triple))

        if k < z - 1:
            new_triple = (i, j, k + 1)
            if new_triple not in check:
                check.add(new_triple)
                s, _ = get(*new_triple)
                heapq.heappush(q, (-s, new_triple))

        next_s, next_triple = heapq.heappop(q)
        ans.append((-next_s, next_triple))
        # print(ans)

    for s, _ in ans:
        print(s)
        

submit()
