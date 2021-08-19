s = input()
query_time = int(input())
queries = [list([int(x) - 1 for x in input().split()]) for _ in range(query_time)]
k = 0
f = [0]
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        k += 1
    f.append(k)
for query in queries:
    (begin, end) = query
    repeat = f[end] - f[begin]
    print(repeat)
