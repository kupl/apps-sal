n, k = [int(x) for x in input().split()]
requests = [int(x) for x in input().split()]

req_list = {}


def find_last(bucket):
    last_book = None
    last_date = None
    nonlocal req_list
    i = 0
    for item in bucket:
        #print(item, req_list)
        if last_book is None:
            last_book = item
            if len(req_list[item]) < 1:
                last_date = float('inf')
                return item, i
            else:
                last_date = req_list[item][0]
            index = i
        elif len(req_list[item]) >= 1 and req_list[item][0] > last_date:
            last_book = item
            last_date = req_list[item][0]
            index = i
        elif len(req_list[item]) < 1 and last_date < float('inf'):
            return item, i
        i += 1
    return last_book, index


def update_reqlist(book):
    nonlocal req_list
    req_list[book] = req_list[book][1:]


for i in range(n):
    if requests[i] in req_list:
        req_list[requests[i]].append(i)
    else:
        req_list[requests[i]] = [i]

bucket = []
bucket_size = 0
cost = 0
for book in requests:
    if book in bucket:
        update_reqlist(book)
        continue
    if bucket_size < k:
        bucket.append(book)
        bucket_size += 1
        cost += 1
        update_reqlist(book)
    else:
        last_book, index = find_last(bucket)
        if len(bucket) > 1:
            bucket.pop(index)
        else:
            bucket = []
        bucket.append(book)
        update_reqlist(book)
        cost += 1
    #print(bucket, req_list)

# print(req_list)
print(cost)
