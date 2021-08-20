n = int(input())
answer = set(list(map(int, input().split()))[1:])
for i in range(n - 1):
    arr = list(map(int, input().split()))[1:]
    buff = set(arr)
    answer = answer.intersection(buff)
print(*answer)
