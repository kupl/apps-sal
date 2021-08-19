magic_string = input()
query_count = int(input())
queries = []
for i in range(query_count):
    queries.append([int(x) for x in input().split()])
saved = [0]
for i in range(1, len(magic_string)):
    saved.append(saved[i - 1] + (1 if magic_string[i - 1] == magic_string[i] else 0))
for query in queries:
    print(saved[query[1] - 1] - saved[query[0] - 1])
