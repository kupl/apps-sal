from collections import deque
from collections import namedtuple
Query = namedtuple("Query", ["time", "duration"])
query_number, max_query_queue_length = list(map(int, input().split()))
queries = deque(Query(*list(map(int, input().split()))) for i in range(query_number))
results = {}
query_queue = deque()
current_time = 0
while len(results) != query_number:
    if query_queue:
        query = query_queue.popleft()
    else:
        query = queries.popleft()
    if current_time > query.time:
        current_time += query.duration
    else:
        current_time = query.time + query.duration
    results[query.time] = current_time
    while queries and queries[0].time < current_time:
        if len(query_queue) < max_query_queue_length:
            query_queue.append(queries.popleft())
        else:
            ignored_query = queries.popleft()
            results[ignored_query.time] = -1
print(" ".join(str(results[time]) for time in sorted(results.keys())))
