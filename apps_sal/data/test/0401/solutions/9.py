n, m = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
first.sort()
second.sort()
if len((set(map(int, first)) & set(map(int, second)))):
    print(min((set(map(int, first)) & set(map(int, second)))))
else:
    f = min(first[0], second[0])
    s = max(first[0], second[0])
    print(f * 10 + s)
