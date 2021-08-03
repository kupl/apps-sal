
n, k, q = list(map(int, input().split()))

t = list(map(int, input().split()))

res = set()
data = []

for _ in range(q):
    req_type, req_id = list(map(int, input().split()))

    if req_type == 1:
        req_t = t[req_id - 1]
        data.append((req_id, req_t))
        res.add(req_id)

        if len(res) > k:
            data = sorted(data, key=lambda x: x[1], reverse=True)
            last = data[-1]
            data = data[:-1]

            res.remove(last[0])

    if req_type == 2:
        if req_id in res:
            print('YES')
        else:
            print('NO')
